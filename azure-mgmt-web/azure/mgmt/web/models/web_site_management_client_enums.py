# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class DomainStatus(Enum):

    active = "Active"
    awaiting = "Awaiting"
    cancelled = "Cancelled"
    confiscated = "Confiscated"
    disabled = "Disabled"
    excluded = "Excluded"
    expired = "Expired"
    failed = "Failed"
    held = "Held"
    locked = "Locked"
    parked = "Parked"
    pending = "Pending"
    reserved = "Reserved"
    reverted = "Reverted"
    suspended = "Suspended"
    transferred = "Transferred"
    unknown = "Unknown"
    unlocked = "Unlocked"
    unparked = "Unparked"
    updated = "Updated"
    json_converter_failed = "JsonConverterFailed"


class ProvisioningState(Enum):

    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    in_progress = "InProgress"
    deleting = "Deleting"


class AzureResourceType(Enum):

    website = "Website"
    traffic_manager = "TrafficManager"


class CustomHostNameDnsRecordType(Enum):

    cname = "CName"
    a = "A"


class HostNameType(Enum):

    verified = "Verified"
    managed = "Managed"


class StatusOptions(Enum):

    ready = "Ready"
    pending = "Pending"


class UsageState(Enum):

    normal = "Normal"
    exceeded = "Exceeded"


class SiteAvailabilityState(Enum):

    normal = "Normal"
    limited = "Limited"
    disaster_recovery_mode = "DisasterRecoveryMode"


class SslState(Enum):

    disabled = "Disabled"
    sni_enabled = "SniEnabled"
    ip_based_enabled = "IpBasedEnabled"


class DatabaseServerType(Enum):

    my_sql = "MySql"
    sql_server = "SQLServer"
    sql_azure = "SQLAzure"
    custom = "Custom"


class ManagedPipelineMode(Enum):

    integrated = "Integrated"
    classic = "Classic"


class SiteLoadBalancing(Enum):

    weighted_round_robin = "WeightedRoundRobin"
    least_requests = "LeastRequests"
    least_response_time = "LeastResponseTime"
    weighted_total_traffic = "WeightedTotalTraffic"
    request_hash = "RequestHash"


class AutoHealActionType(Enum):

    recycle = "Recycle"
    log_event = "LogEvent"
    custom_action = "CustomAction"


class UnauthenticatedClientAction(Enum):

    redirect_to_login_page = "RedirectToLoginPage"
    allow_anonymous = "AllowAnonymous"


class BuiltInAuthenticationProvider(Enum):

    azure_active_directory = "AzureActiveDirectory"
    facebook = "Facebook"
    google = "Google"
    microsoft_account = "MicrosoftAccount"
    twitter = "Twitter"


class HostingEnvironmentStatus(Enum):

    preparing = "Preparing"
    ready = "Ready"
    scaling = "Scaling"
    deleting = "Deleting"


class InternalLoadBalancingMode(Enum):

    none = "None"
    web = "Web"
    publishing = "Publishing"


class ComputeModeOptions(Enum):

    shared = "Shared"
    dedicated = "Dedicated"


class WorkerSizeOptions(Enum):

    default = "Default"
    small = "Small"
    medium = "Medium"
    large = "Large"


class AccessControlEntryAction(Enum):

    permit = "Permit"
    deny = "Deny"


class ManagedHostingEnvironmentStatus(Enum):

    preparing = "Preparing"
    ready = "Ready"
    deleting = "Deleting"


class DomainType(Enum):

    regular = "Regular"
    soft_deleted = "SoftDeleted"


class NotificationLevel(Enum):

    critical = "Critical"
    warning = "Warning"
    information = "Information"
    non_urgent_suggestion = "NonUrgentSuggestion"


class Channels(Enum):

    notification = "Notification"
    api = "Api"
    email = "Email"
    all = "All"


class CloneAbilityResult(Enum):

    cloneable = "Cloneable"
    partially_cloneable = "PartiallyCloneable"
    not_cloneable = "NotCloneable"


class LogLevel(Enum):

    off = "Off"
    verbose = "Verbose"
    information = "Information"
    warning = "Warning"
    error = "Error"


class FrequencyUnit(Enum):

    day = "Day"
    hour = "Hour"


class BackupRestoreOperationType(Enum):

    default = "Default"
    clone = "Clone"
    relocation = "Relocation"


class BackupItemStatus(Enum):

    in_progress = "InProgress"
    failed = "Failed"
    succeeded = "Succeeded"
    timed_out = "TimedOut"
    created = "Created"
    skipped = "Skipped"
    partially_succeeded = "PartiallySucceeded"
    delete_in_progress = "DeleteInProgress"
    delete_failed = "DeleteFailed"
    deleted = "Deleted"