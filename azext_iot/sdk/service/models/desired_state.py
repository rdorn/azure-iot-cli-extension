# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DesiredState(Model):
    """DesiredState.

    :param code: Status code for the operation.
    :type code: int
    :param sub_code: Sub status code for the status.
    :type sub_code: int
    :param version: Version of the desired value received.
    :type version: long
    :param description: Description of the status.
    :type description: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'sub_code': {'key': 'subCode', 'type': 'int'},
        'version': {'key': 'version', 'type': 'long'},
        'description': {'key': 'description', 'type': 'str'},
    }

    def __init__(self, code=None, sub_code=None, version=None, description=None):
        super(DesiredState, self).__init__()
        self.code = code
        self.sub_code = sub_code
        self.version = version
        self.description = description