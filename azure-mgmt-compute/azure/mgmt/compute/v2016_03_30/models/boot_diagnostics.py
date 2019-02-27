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


class BootDiagnostics(Model):
    """Boot Diagnostics is a debugging feature which allows you to view Console
    Output and Screenshot to diagnose VM status. <br><br> You can easily view
    the output of your console log. <br><br> Azure also enables you to see a
    screenshot of the VM from the hypervisor.

    :param enabled: Whether boot diagnostics should be enabled on the Virtual
     Machine.
    :type enabled: bool
    :param storage_uri: Uri of the storage account to use for placing the
     console output and screenshot.
    :type storage_uri: str
    """

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'storage_uri': {'key': 'storageUri', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(BootDiagnostics, self).__init__(**kwargs)
        self.enabled = kwargs.get('enabled', None)
        self.storage_uri = kwargs.get('storage_uri', None)
