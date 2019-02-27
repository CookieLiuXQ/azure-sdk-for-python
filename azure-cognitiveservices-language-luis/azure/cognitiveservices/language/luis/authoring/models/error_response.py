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
from msrest.exceptions import HttpOperationError


class ErrorResponse(Model):
    """Error response when invoking an operation on the API.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param error_type:
    :type error_type: str
    """

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'error_type': {'key': 'errorType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.additional_properties = kwargs.get('additional_properties', None)
        self.error_type = kwargs.get('error_type', None)


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)
