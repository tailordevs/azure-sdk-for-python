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


class BMSContainerQueryObject(Model):
    """The query filters that can be used with the list containers API.

    :param backup_management_type: Backup management type for this container.
     Possible values include: 'Invalid', 'AzureIaasVM', 'MAB', 'DPM',
     'AzureBackupServer', 'AzureSql'
    :type backup_management_type: str or :class:`BackupManagementType
     <azure.mgmt.recoveryservicesbackup.models.BackupManagementType>`
    :param container_type: Type of container for filter. Possible values
     include: 'Invalid', 'Unknown', 'IaasVMContainer',
     'IaasVMServiceContainer', 'DPMContainer', 'AzureBackupServerContainer',
     'MABContainer', 'Cluster', 'AzureSqlContainer', 'Windows', 'VCenter'
    :type container_type: str or :class:`ContainerType
     <azure.mgmt.recoveryservicesbackup.models.ContainerType>`
    :param backup_engine_name: Backup engine name
    :type backup_engine_name: str
    :param status: Status of registration of this container with the Recovery
     Services Vault.
    :type status: str
    :param friendly_name: Friendly name of this container.
    :type friendly_name: str
    """

    _validation = {
        'backup_management_type': {'required': True},
    }

    _attribute_map = {
        'backup_management_type': {'key': 'backupManagementType', 'type': 'str'},
        'container_type': {'key': 'containerType', 'type': 'str'},
        'backup_engine_name': {'key': 'backupEngineName', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'friendly_name': {'key': 'friendlyName', 'type': 'str'},
    }

    def __init__(self, backup_management_type, container_type=None, backup_engine_name=None, status=None, friendly_name=None):
        self.backup_management_type = backup_management_type
        self.container_type = container_type
        self.backup_engine_name = backup_engine_name
        self.status = status
        self.friendly_name = friendly_name
