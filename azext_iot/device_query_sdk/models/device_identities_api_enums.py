# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class QueryResultType(Enum):

    unknown = "unknown"
    twin = "twin"
    device_job = "deviceJob"
    job_response = "jobResponse"
    raw = "raw"


class DeviceConnectionState(Enum):

    disconnected = "disconnected"
    connected = "connected"


class DeviceStatus(Enum):

    enabled = "enabled"
    disabled = "disabled"


class ErrorCode(Enum):

    invalid_error_code = "InvalidErrorCode"
    invalid_protocol_version = "InvalidProtocolVersion"
    device_invalid_result_count = "DeviceInvalidResultCount"
    invalid_operation = "InvalidOperation"
    argument_invalid = "ArgumentInvalid"
    argument_null = "ArgumentNull"
    iot_hub_format_error = "IotHubFormatError"
    device_storage_entity_serialization_error = "DeviceStorageEntitySerializationError"
    blob_container_validation_error = "BlobContainerValidationError"
    import_warning_exists_error = "ImportWarningExistsError"
    invalid_schema_version = "InvalidSchemaVersion"
    device_defined_multiple_times = "DeviceDefinedMultipleTimes"
    deserialization_error = "DeserializationError"
    bulk_registry_operation_failure = "BulkRegistryOperationFailure"
    default_storage_endpoint_not_configured = "DefaultStorageEndpointNotConfigured"
    invalid_file_upload_correlation_id = "InvalidFileUploadCorrelationId"
    expired_file_upload_correlation_id = "ExpiredFileUploadCorrelationId"
    invalid_storage_endpoint = "InvalidStorageEndpoint"
    invalid_messaging_endpoint = "InvalidMessagingEndpoint"
    invalid_file_upload_completion_status = "InvalidFileUploadCompletionStatus"
    invalid_storage_endpoint_or_blob = "InvalidStorageEndpointOrBlob"
    request_canceled = "RequestCanceled"
    invalid_storage_endpoint_property = "InvalidStorageEndpointProperty"
    invalid_route_test_input = "InvalidRouteTestInput"
    invalid_source_on_route = "InvalidSourceOnRoute"
    iot_hub_not_found = "IotHubNotFound"
    iot_hub_unauthorized_access = "IotHubUnauthorizedAccess"
    iot_hub_unauthorized = "IotHubUnauthorized"
    iot_hub_suspended = "IotHubSuspended"
    iot_hub_quota_exceeded = "IotHubQuotaExceeded"
    job_quota_exceeded = "JobQuotaExceeded"
    device_maximum_queue_depth_exceeded = "DeviceMaximumQueueDepthExceeded"
    iot_hub_max_cbs_token_exceeded = "IotHubMaxCbsTokenExceeded"
    device_maximum_active_file_upload_limit_exceeded = "DeviceMaximumActiveFileUploadLimitExceeded"
    device_maximum_queue_size_exceeded = "DeviceMaximumQueueSizeExceeded"
    device_model_max_properties_exceeded = "DeviceModelMaxPropertiesExceeded"
    device_model_max_indexable_properties_exceeded = "DeviceModelMaxIndexablePropertiesExceeded"
    device_not_found = "DeviceNotFound"
    job_not_found = "JobNotFound"
    partition_not_found = "PartitionNotFound"
    quota_metric_not_found = "QuotaMetricNotFound"
    system_property_not_found = "SystemPropertyNotFound"
    amqp_address_not_found = "AmqpAddressNotFound"
    query_store_cluster_not_found = "QueryStoreClusterNotFound"
    device_not_online = "DeviceNotOnline"
    operation_not_allowed_in_current_state = "OperationNotAllowedInCurrentState"
    import_devices_not_supported = "ImportDevicesNotSupported"
    bulk_add_devices_not_supported = "BulkAddDevicesNotSupported"
    device_already_exists = "DeviceAlreadyExists"
    link_creation_conflict = "LinkCreationConflict"
    model_already_exists = "ModelAlreadyExists"
    device_locked = "DeviceLocked"
    device_job_already_exists = "DeviceJobAlreadyExists"
    precondition_failed = "PreconditionFailed"
    device_message_lock_lost = "DeviceMessageLockLost"
    job_run_precondition_failed = "JobRunPreconditionFailed"
    message_too_large = "MessageTooLarge"
    too_many_devices = "TooManyDevices"
    incompatible_data_type = "IncompatibleDataType"
    throttling_exception = "ThrottlingException"
    throttle_backlog_limit_exceeded = "ThrottleBacklogLimitExceeded"
    throttling_backlog_timeout = "ThrottlingBacklogTimeout"
    throttling_max_active_job_count_exceeded = "ThrottlingMaxActiveJobCountExceeded"
    server_error = "ServerError"
    job_cancelled = "JobCancelled"
    statistics_retrieval_error = "StatisticsRetrievalError"
    connection_forcefully_closed = "ConnectionForcefullyClosed"
    invalid_blob_state = "InvalidBlobState"
    backup_timed_out = "BackupTimedOut"
    azure_storage_timeout = "AzureStorageTimeout"
    generic_timeout = "GenericTimeout"
    invalid_throttle_parameter = "InvalidThrottleParameter"
    event_hub_link_already_closed = "EventHubLinkAlreadyClosed"
    reliable_blob_store_error = "ReliableBlobStoreError"
    retry_attempts_exhausted = "RetryAttemptsExhausted"
    unexpected_property_value = "UnexpectedPropertyValue"
    orchestration_operation_failed = "OrchestrationOperationFailed"
    invalid_response_while_proxying = "InvalidResponseWhileProxying"
    service_unavailable = "ServiceUnavailable"
    iot_hub_failing_over = "IotHubFailingOver"
    connection_unavailable = "ConnectionUnavailable"
    device_unavailable = "DeviceUnavailable"
    gateway_timeout = "GatewayTimeout"


class ProvisioningState(Enum):

    creating = "Creating"
    deleting = "Deleting"
    active = "Active"
    deleted = "Deleted"