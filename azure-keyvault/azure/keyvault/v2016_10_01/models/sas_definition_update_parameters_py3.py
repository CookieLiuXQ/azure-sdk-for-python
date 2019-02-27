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


class SasDefinitionUpdateParameters(Model):
    """The SAS definition update parameters.

    :param parameters: Sas definition update metadata in the form of key-value
     pairs.
    :type parameters: dict[str, str]
    :param sas_definition_attributes: The attributes of the SAS definition.
    :type sas_definition_attributes:
     ~azure.keyvault.v2016_10_01.models.SasDefinitionAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'parameters': {'key': 'parameters', 'type': '{str}'},
        'sas_definition_attributes': {'key': 'attributes', 'type': 'SasDefinitionAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, parameters=None, sas_definition_attributes=None, tags=None, **kwargs) -> None:
        super(SasDefinitionUpdateParameters, self).__init__(**kwargs)
        self.parameters = parameters
        self.sas_definition_attributes = sas_definition_attributes
        self.tags = tags
