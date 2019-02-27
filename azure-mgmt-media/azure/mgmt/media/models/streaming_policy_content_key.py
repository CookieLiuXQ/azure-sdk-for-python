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


class StreamingPolicyContentKey(Model):
    """Class to specify properties of content key.

    :param label: Label can be used to specify Content Key when creating a
     Streaming Locator
    :type label: str
    :param policy_name: Policy used by Content Key
    :type policy_name: str
    :param tracks: Tracks which use this content key
    :type tracks: list[~azure.mgmt.media.models.TrackSelection]
    """

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'policy_name': {'key': 'policyName', 'type': 'str'},
        'tracks': {'key': 'tracks', 'type': '[TrackSelection]'},
    }

    def __init__(self, **kwargs):
        super(StreamingPolicyContentKey, self).__init__(**kwargs)
        self.label = kwargs.get('label', None)
        self.policy_name = kwargs.get('policy_name', None)
        self.tracks = kwargs.get('tracks', None)
