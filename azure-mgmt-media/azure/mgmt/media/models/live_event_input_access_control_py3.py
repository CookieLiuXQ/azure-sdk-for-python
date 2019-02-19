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


class LiveEventInputAccessControl(Model):
    """The IP access control for Live Event Input.

    :param ip: The IP access control properties.
    :type ip: ~azure.mgmt.media.models.IPAccessControl
    """

    _attribute_map = {
        'ip': {'key': 'ip', 'type': 'IPAccessControl'},
    }

    def __init__(self, *, ip=None, **kwargs) -> None:
        super(LiveEventInputAccessControl, self).__init__(**kwargs)
        self.ip = ip
