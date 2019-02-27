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


class ImageMetadata(Model):
    """Image metadata.

    :param width: Image width
    :type width: int
    :param height: Image height
    :type height: int
    :param format: Image format
    :type format: str
    """

    _attribute_map = {
        'width': {'key': 'width', 'type': 'int'},
        'height': {'key': 'height', 'type': 'int'},
        'format': {'key': 'format', 'type': 'str'},
    }

    def __init__(self, *, width: int=None, height: int=None, format: str=None, **kwargs) -> None:
        super(ImageMetadata, self).__init__(**kwargs)
        self.width = width
        self.height = height
        self.format = format
