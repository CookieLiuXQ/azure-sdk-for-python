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

from .catalog_item_py3 import CatalogItem


class USqlSecret(CatalogItem):
    """A Data Lake Analytics catalog U-SQL secret item.

    :param compute_account_name: the name of the Data Lake Analytics account.
    :type compute_account_name: str
    :param version: the version of the catalog item.
    :type version: str
    :param database_name: the name of the database.
    :type database_name: str
    :param name: the name of the secret.
    :type name: str
    :param creation_time: the creation time of the credential object. This is
     the only information returned about a secret from a GET.
    :type creation_time: datetime
    :param uri: the URI identifier for the secret in the format
     <hostname>:<port>
    :type uri: str
    :param password: the password for the secret to pass in
    :type password: str
    """

    _attribute_map = {
        'compute_account_name': {'key': 'computeAccountName', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
        'name': {'key': 'secretName', 'type': 'str'},
        'creation_time': {'key': 'creationTime', 'type': 'iso-8601'},
        'uri': {'key': 'uri', 'type': 'str'},
        'password': {'key': 'password', 'type': 'str'},
    }

    def __init__(self, *, compute_account_name: str=None, version: str=None, database_name: str=None, name: str=None, creation_time=None, uri: str=None, password: str=None, **kwargs) -> None:
        super(USqlSecret, self).__init__(compute_account_name=compute_account_name, version=version, **kwargs)
        self.database_name = database_name
        self.name = name
        self.creation_time = creation_time
        self.uri = uri
        self.password = password
