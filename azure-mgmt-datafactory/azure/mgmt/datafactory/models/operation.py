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


class Operation(Model):
    """Azure Data Factory API operation definition.

    :param name: Operation name: {provider}/{resource}/{operation}
    :type name: str
    :param origin: The intended executor of the operation.
    :type origin: str
    :param display: Metadata associated with the operation.
    :type display: :class:`OperationDisplay
     <azure.mgmt.datafactory.models.OperationDisplay>`
    :param service_specification: Details about a service operation.
    :type service_specification: :class:`OperationServiceSpecification
     <azure.mgmt.datafactory.models.OperationServiceSpecification>`
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'origin': {'key': 'origin', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
        'service_specification': {'key': 'properties.serviceSpecification', 'type': 'OperationServiceSpecification'},
    }

    def __init__(self, name=None, origin=None, display=None, service_specification=None):
        self.name = name
        self.origin = origin
        self.display = display
        self.service_specification = service_specification
