# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os
import time

from azure.cli.testsdk import LiveScenarioTest
from azext_iot.central.models.enum import DeviceStatus
from azext_iot.common import utility

APP_ID = os.environ.get("azext_iot_central_app_id")
DEVICE_TEMPLATE_PATH = os.environ.get("azext_iot_central_device_template_path")

if not all([APP_ID, DEVICE_TEMPLATE_PATH]):
    raise ValueError(
        "Set azext_iot_central_app_id, azext_iot_central_device_template_path"
        "to run central integration tests. "
    )


class TestIotCentral(LiveScenarioTest):
    def __init__(self, test_case):
        super(TestIotCentral, self).__init__(test_case)

    def test_central_device_twin_show_fail(self):
        (device_id, _) = self._create_device()

        # Verify incorrect app-id throws error
        self.cmd(
            "iotcentral device-twin show --app-id incorrect-app --device-id {}".format(
                device_id
            ),
            expect_failure=True,
        )
        # Verify incorrect device-id throws error
        self.cmd(
            "iotcentral device-twin show --app-id {} --device-id incorrect-device".format(
                APP_ID
            ),
            expect_failure=True,
        )

        # Verify incorrect app-id throws error
        self.cmd(
            "iot central app device-twin show --app-id incorrect-app --device-id {}".format(
                device_id
            ),
            expect_failure=True,
        )
        # Verify incorrect device-id throws error
        self.cmd(
            "iot central app device-twin show --app-id {} --device-id incorrect-device".format(
                APP_ID
            ),
            expect_failure=True,
        )

        self._delete_device(device_id)

    def test_central_device_twin_show_success(self):
        (template_id, _) = self._create_device_template()
        (device_id, _) = self._create_device(instance_of=template_id, simulated=True)

        # wait about a few seconds for simulator to kick in so that provisioning completes
        time.sleep(60)

        self.cmd(
            "iotcentral device-twin show --app-id {} --device-id {}".format(
                APP_ID, device_id
            ),
            checks=[self.check("deviceId", device_id)],
        )

        self.cmd(
            "iot central app device-twin show --app-id {} --device-id {}".format(
                APP_ID, device_id
            ),
            checks=[self.check("deviceId", device_id)],
        )

        self._delete_device(device_id)
        self._delete_device_template(template_id)

    def test_central_monitor_events(self):
        # Test with invalid app-id
        self.cmd(
            "iotcentral app monitor-events --app-id {}".format(APP_ID + "zzz"),
            expect_failure=True,
        )
        # Ensure no failure
        # We cannot verify that the result is correct, as the Azure CLI for IoT Central does not support adding devices
        self.cmd("iotcentral app monitor-events --app-id {} --to 1".format(APP_ID))

    def test_central_validate_messages(self):
        # Test with invalid app-id
        self.cmd(
            "iot central app validate-messages --app-id {}".format(APP_ID + "zzz"),
            expect_failure=True,
        )
        # Ensure no failure
        # We cannot verify that the result is correct, as the Azure CLI for IoT Central does not support adding devices
        self.cmd("iot central app validate-messages --app-id {} --to 1".format(APP_ID))

    def test_central_device_methods_CRLD(self):
        (device_id, device_name) = self._create_device()

        self.cmd(
            "iot central app device show --app-id {} -d {}".format(APP_ID, device_id),
            checks=[
                self.check("approved", True),
                self.check("displayName", device_name),
                self.check("id", device_id),
                self.check("simulated", False),
            ],
        )

        list_output = self.cmd("iot central app device list --app-id {}".format(APP_ID))

        self._delete_device(device_id)

        assert device_id in list_output.get_output_in_json()

    def test_central_device_template_methods_CRLD(self):
        # currently: create, show, list, delete
        (template_id, template_name) = self._create_device_template()

        self.cmd(
            "iot central app device-template show --app-id {} --device-template-id {}".format(
                APP_ID, template_id
            ),
            checks=[
                self.check("displayName", template_name),
                self.check("id", template_id),
            ],
        )

        list_output = self.cmd(
            "iot central app device-template list --app-id {}".format(APP_ID)
        )
        map_output = self.cmd(
            "iot central app device-template map --app-id {}".format(APP_ID)
        )

        self._delete_device_template(template_id)

        assert template_id in list_output.get_output_in_json()

        map_json = map_output.get_output_in_json()
        assert map_json[template_name] == template_id

    def test_central_device_registration_info_registered(self):
        (template_id, _) = self._create_device_template()
        (device_id, device_name) = self._create_device(
            instance_of=template_id, simulated=False
        )

        result = self.cmd(
            "iot central app device registration-info --app-id {} -d {}".format(
                APP_ID, device_id
            )
        )

        self._delete_device(device_id)
        self._delete_device_template(template_id)

        json_result = result.get_output_in_json()

        assert json_result["@device_id"] == device_id

        # since time taken for provisioning to complete is not known
        # we can only assert that the payload is populated, not anything specific beyond that
        assert json_result["device_registration_info"] is not None
        assert json_result["dps_state"] is not None

        # Validation - device registration.
        device_registration_info = json_result["device_registration_info"]
        assert len(device_registration_info) == 5
        assert device_registration_info.get("device_status") == "registered"
        assert device_registration_info.get("id") == device_id
        assert device_registration_info.get("display_name") == device_name
        assert device_registration_info.get("instance_of") == template_id
        assert not device_registration_info.get("simulated")

        # Validation - dps state
        dps_state = json_result["dps_state"]
        assert len(dps_state) == 2
        assert device_registration_info.get("status") is None
        assert dps_state.get("error") == "Device is not yet provisioned."

    def test_central_device_registration_info_unassociated(self):

        (device_id, device_name) = self._create_device()

        result = self.cmd(
            "iot central app device registration-info --app-id {} -d {}".format(
                APP_ID, device_id
            )
        )

        self._delete_device(device_id)

        json_result = result.get_output_in_json()

        assert json_result["@device_id"] == device_id

        # since time taken for provisioning to complete is not known
        # we can only assert that the payload is populated, not anything specific beyond that
        assert json_result["device_registration_info"] is not None
        assert json_result["dps_state"] is not None

        # Validation - device registration.
        device_registration_info = json_result["device_registration_info"]
        assert len(device_registration_info) == 5
        assert device_registration_info.get("device_status") == "unassociated"
        assert device_registration_info.get("id") == device_id
        assert device_registration_info.get("display_name") == device_name
        assert device_registration_info.get("instance_of") is None
        assert not device_registration_info.get("simulated")

        # Validation - dps state
        dps_state = json_result["dps_state"]
        assert len(dps_state) == 2
        assert device_registration_info.get("status") is None
        assert (
            dps_state.get("error")
            == "Device does not have a valid template associated with it."
        )

    def test_central_device_registration_summary(self):

        result = self.cmd(
            "iot central app device registration-summary --app-id {}".format(APP_ID,)
        )

        json_result = result.get_output_in_json()
        assert json_result[DeviceStatus.provisioned.value] is not None
        assert json_result[DeviceStatus.registered.value] is not None
        assert json_result[DeviceStatus.unassociated.value] is not None
        assert json_result[DeviceStatus.blocked.value] is not None
        assert len(json_result) == 4

    def _create_device(self, **kwargs) -> (str, str):
        """
        kwargs:
            instance_of: template_id (str)
            simulated: if the device is to be simulated (bool)
        """
        device_id = self.create_random_name(prefix="aztest", length=24)
        device_name = self.create_random_name(prefix="aztest", length=24)

        command = "iot central app device create --app-id {} -d {} --device-name {}".format(
            APP_ID, device_id, device_name
        )
        checks = [
            self.check("approved", True),
            self.check("displayName", device_name),
            self.check("id", device_id),
        ]

        instance_of = kwargs.get("instance_of")
        if instance_of:
            command = command + " --instance-of {}".format(instance_of)
            checks.append(self.check("instanceOf", instance_of))

        simulated = bool(kwargs.get("simulated"))
        if simulated:
            command = command + " --simulated"

        checks.append(self.check("simulated", simulated))

        self.cmd(command, checks=checks)
        return (device_id, device_name)

    def _delete_device(self, device_id) -> None:
        self.cmd(
            "iot central app device delete --app-id {} -d {}".format(APP_ID, device_id),
            checks=[self.check("result", "success")],
        )

    def _create_device_template(self):
        template = utility.process_json_arg(
            DEVICE_TEMPLATE_PATH, argument_name="DEVICE_TEMPLATE_PATH"
        )
        template_name = template["displayName"]
        template_id = template_name + "id"

        self.cmd(
            "iot central app device-template create --app-id {} --device-template-id {} -k {}".format(
                APP_ID, template_id, DEVICE_TEMPLATE_PATH
            ),
            checks=[
                self.check("displayName", template_name),
                self.check("id", template_id),
            ],
        )

        return (template_id, template_name)

    def _delete_device_template(self, template_id):
        self.cmd(
            "iot central app device-template delete --app-id {} --device-template-id {}".format(
                APP_ID, template_id
            ),
            checks=[self.check("result", "success")],
        )
