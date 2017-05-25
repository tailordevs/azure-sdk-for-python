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


class SasDefinitionBundle(Model):
    """A sas definition bundle consists of key vault sas definition details plus
    its attributes.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The sas definition id.
    :vartype id: str
    :ivar secret_id: Storage account sas definition secret id.
    :vartype secret_id: str
    :ivar parameters: The sas definition metadata in the form of key-value
     pairs.
    :vartype parameters: dict
    :ivar attributes: The sas definition attributes.
    :vartype attributes: :class:`SasDefinitionAttributes
     <azure.keyvault.models.SasDefinitionAttributes>`
    :ivar tags: Application specific metadata in the form of key-value pairs
    :vartype tags: dict
    """

    _validation = {
        'id': {'readonly': True},
        'secret_id': {'readonly': True},
        'parameters': {'readonly': True},
        'attributes': {'readonly': True},
        'tags': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'secret_id': {'key': 'sid', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'attributes': {'key': 'attributes', 'type': 'SasDefinitionAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self):
        self.id = None
        self.secret_id = None
        self.parameters = None
        self.attributes = None
        self.tags = None