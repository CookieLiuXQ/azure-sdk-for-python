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

from .model_info_py3 import ModelInfo


class IntentClassifier(ModelInfo):
    """Intent Classifier.

    All required parameters must be populated in order to send to Azure.

    :param id: Required. The ID of the Entity Model.
    :type id: str
    :param name: Name of the Entity Model.
    :type name: str
    :param type_id: The type ID of the Entity Model.
    :type type_id: int
    :param readable_type: Required. Possible values include: 'Entity
     Extractor', 'Hierarchical Entity Extractor', 'Hierarchical Child Entity
     Extractor', 'Composite Entity Extractor', 'Closed List Entity Extractor',
     'Prebuilt Entity Extractor', 'Intent Classifier', 'Pattern.Any Entity
     Extractor', 'Regex Entity Extractor'
    :type readable_type: str or
     ~azure.cognitiveservices.language.luis.authoring.models.enum
    :param custom_prebuilt_domain_name: The domain name.
    :type custom_prebuilt_domain_name: str
    :param custom_prebuilt_model_name: The intent name or entity name.
    :type custom_prebuilt_model_name: str
    """

    _validation = {
        'id': {'required': True},
        'readable_type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type_id': {'key': 'typeId', 'type': 'int'},
        'readable_type': {'key': 'readableType', 'type': 'str'},
        'custom_prebuilt_domain_name': {'key': 'customPrebuiltDomainName', 'type': 'str'},
        'custom_prebuilt_model_name': {'key': 'customPrebuiltModelName', 'type': 'str'},
    }

    def __init__(self, *, id: str, readable_type, name: str=None, type_id: int=None, custom_prebuilt_domain_name: str=None, custom_prebuilt_model_name: str=None, **kwargs) -> None:
        super(IntentClassifier, self).__init__(id=id, name=name, type_id=type_id, readable_type=readable_type, **kwargs)
        self.custom_prebuilt_domain_name = custom_prebuilt_domain_name
        self.custom_prebuilt_model_name = custom_prebuilt_model_name
