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


class CaptureDescription(Model):
    """Properties to configure capture description for eventhub.

    :param enabled: A value that indicates whether capture description is
     enabled.
    :type enabled: bool
    :param encoding: Enumerates the possible values for the encoding format of
     capture description. Note: 'AvroDeflate' will be deprecated in New API
     Version. Possible values include: 'Avro', 'AvroDeflate'
    :type encoding: str or
     ~azure.mgmt.eventhub.models.EncodingCaptureDescription
    :param interval_in_seconds: The time window allows you to set the
     frequency with which the capture to Azure Blobs will happen, value should
     between 60 to 900 seconds
    :type interval_in_seconds: int
    :param size_limit_in_bytes: The size window defines the amount of data
     built up in your Event Hub before an capture operation, value should be
     between 10485760 to 524288000 bytes
    :type size_limit_in_bytes: int
    :param destination: Properties of Destination where capture will be
     stored. (Storage Account, Blob Names)
    :type destination: ~azure.mgmt.eventhub.models.Destination
    :param skip_empty_archives: A value that indicates whether to Skip Empty
     Archives
    :type skip_empty_archives: bool
    """

    _validation = {
        'interval_in_seconds': {'maximum': 900, 'minimum': 60},
        'size_limit_in_bytes': {'maximum': 524288000, 'minimum': 10485760},
    }

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'encoding': {'key': 'encoding', 'type': 'EncodingCaptureDescription'},
        'interval_in_seconds': {'key': 'intervalInSeconds', 'type': 'int'},
        'size_limit_in_bytes': {'key': 'sizeLimitInBytes', 'type': 'int'},
        'destination': {'key': 'destination', 'type': 'Destination'},
        'skip_empty_archives': {'key': 'skipEmptyArchives', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(CaptureDescription, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', None)
        self.encoding = kwargs.get('encoding', None)
        self.interval_in_seconds = kwargs.get('interval_in_seconds', None)
        self.size_limit_in_bytes = kwargs.get('size_limit_in_bytes', None)
        self.destination = kwargs.get('destination', None)
        self.skip_empty_archives = kwargs.get('skip_empty_archives', None)
