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

from .linked_service import LinkedService


class HdfsLinkedService(LinkedService):
    """Hadoop Distributed File System (HDFS) linked service.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     Dataset.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param url: Required. The URL of the HDFS service endpoint, e.g.
     http://myhostname:50070/webhdfs/v1 . Type: string (or Expression with
     resultType string).
    :type url: object
    :param authentication_type: Type of authentication used to connect to the
     HDFS. Possible values are: Anonymous and Windows. Type: string (or
     Expression with resultType string).
    :type authentication_type: object
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    :param user_name: User name for Windows authentication. Type: string (or
     Expression with resultType string).
    :type user_name: object
    :param password: Password for Windows authentication.
    :type password: ~azure.mgmt.datafactory.models.SecretBase
    """

    _validation = {
        'type': {'required': True},
        'url': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'typeProperties.url', 'type': 'object'},
        'authentication_type': {'key': 'typeProperties.authenticationType', 'type': 'object'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
        'user_name': {'key': 'typeProperties.userName', 'type': 'object'},
        'password': {'key': 'typeProperties.password', 'type': 'SecretBase'},
    }

    def __init__(self, **kwargs):
        super(HdfsLinkedService, self).__init__(**kwargs)
        self.url = kwargs.get('url', None)
        self.authentication_type = kwargs.get('authentication_type', None)
        self.encrypted_credential = kwargs.get('encrypted_credential', None)
        self.user_name = kwargs.get('user_name', None)
        self.password = kwargs.get('password', None)
        self.type = 'Hdfs'
