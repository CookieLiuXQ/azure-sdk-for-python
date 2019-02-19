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


class ConnectivityHop(Model):
    """Information about a hop between the source and the destination.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The type of the hop.
    :vartype type: str
    :ivar id: The ID of the hop.
    :vartype id: str
    :ivar address: The IP address of the hop.
    :vartype address: str
    :ivar resource_id: The ID of the resource corresponding to this hop.
    :vartype resource_id: str
    :ivar next_hop_ids: List of next hop identifiers.
    :vartype next_hop_ids: list[str]
    :ivar issues: List of issues.
    :vartype issues:
     list[~azure.mgmt.network.v2018_10_01.models.ConnectivityIssue]
    """

    _validation = {
        'type': {'readonly': True},
        'id': {'readonly': True},
        'address': {'readonly': True},
        'resource_id': {'readonly': True},
        'next_hop_ids': {'readonly': True},
        'issues': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'address': {'key': 'address', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'next_hop_ids': {'key': 'nextHopIds', 'type': '[str]'},
        'issues': {'key': 'issues', 'type': '[ConnectivityIssue]'},
    }

    def __init__(self, **kwargs):
        super(ConnectivityHop, self).__init__(**kwargs)
        self.type = None
        self.id = None
        self.address = None
        self.resource_id = None
        self.next_hop_ids = None
        self.issues = None
