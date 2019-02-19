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


class ExpressRouteCircuitArpTable(Model):
    """The ARP table associated with the ExpressRouteCircuit.

    :param age: Entry age in minutes
    :type age: int
    :param interface: Interface address
    :type interface: str
    :param ip_address: The IP address.
    :type ip_address: str
    :param mac_address: The MAC address.
    :type mac_address: str
    """

    _attribute_map = {
        'age': {'key': 'age', 'type': 'int'},
        'interface': {'key': 'interface', 'type': 'str'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'mac_address': {'key': 'macAddress', 'type': 'str'},
    }

    def __init__(self, *, age: int=None, interface: str=None, ip_address: str=None, mac_address: str=None, **kwargs) -> None:
        super(ExpressRouteCircuitArpTable, self).__init__(**kwargs)
        self.age = age
        self.interface = interface
        self.ip_address = ip_address
        self.mac_address = mac_address
