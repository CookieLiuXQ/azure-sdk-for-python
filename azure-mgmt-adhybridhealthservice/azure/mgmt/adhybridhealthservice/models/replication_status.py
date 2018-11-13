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


class ReplicationStatus(Model):
    """Replication summary for a domain controller.

    :param forest_name: The forest name.
    :type forest_name: str
    :param total_dc_count: The total numbe of domain controllers for a given
     forest.
    :type total_dc_count: int
    :param error_dc_count: The total number of domain controllers with error
     in a given forest.
    :type error_dc_count: int
    """

    _attribute_map = {
        'forest_name': {'key': 'forestName', 'type': 'str'},
        'total_dc_count': {'key': 'totalDcCount', 'type': 'int'},
        'error_dc_count': {'key': 'errorDcCount', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(ReplicationStatus, self).__init__(**kwargs)
        self.forest_name = kwargs.get('forest_name', None)
        self.total_dc_count = kwargs.get('total_dc_count', None)
        self.error_dc_count = kwargs.get('error_dc_count', None)
