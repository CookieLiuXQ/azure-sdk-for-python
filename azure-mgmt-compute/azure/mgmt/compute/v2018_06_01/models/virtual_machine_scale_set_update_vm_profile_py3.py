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


class VirtualMachineScaleSetUpdateVMProfile(Model):
    """Describes a virtual machine scale set virtual machine profile.

    :param os_profile: The virtual machine scale set OS profile.
    :type os_profile:
     ~azure.mgmt.compute.v2018_06_01.models.VirtualMachineScaleSetUpdateOSProfile
    :param storage_profile: The virtual machine scale set storage profile.
    :type storage_profile:
     ~azure.mgmt.compute.v2018_06_01.models.VirtualMachineScaleSetUpdateStorageProfile
    :param network_profile: The virtual machine scale set network profile.
    :type network_profile:
     ~azure.mgmt.compute.v2018_06_01.models.VirtualMachineScaleSetUpdateNetworkProfile
    :param diagnostics_profile: The virtual machine scale set diagnostics
     profile.
    :type diagnostics_profile:
     ~azure.mgmt.compute.v2018_06_01.models.DiagnosticsProfile
    :param extension_profile: The virtual machine scale set extension profile.
    :type extension_profile:
     ~azure.mgmt.compute.v2018_06_01.models.VirtualMachineScaleSetExtensionProfile
    :param license_type: The license type, which is for bring your own license
     scenario.
    :type license_type: str
    """

    _attribute_map = {
        'os_profile': {'key': 'osProfile', 'type': 'VirtualMachineScaleSetUpdateOSProfile'},
        'storage_profile': {'key': 'storageProfile', 'type': 'VirtualMachineScaleSetUpdateStorageProfile'},
        'network_profile': {'key': 'networkProfile', 'type': 'VirtualMachineScaleSetUpdateNetworkProfile'},
        'diagnostics_profile': {'key': 'diagnosticsProfile', 'type': 'DiagnosticsProfile'},
        'extension_profile': {'key': 'extensionProfile', 'type': 'VirtualMachineScaleSetExtensionProfile'},
        'license_type': {'key': 'licenseType', 'type': 'str'},
    }

    def __init__(self, *, os_profile=None, storage_profile=None, network_profile=None, diagnostics_profile=None, extension_profile=None, license_type: str=None, **kwargs) -> None:
        super(VirtualMachineScaleSetUpdateVMProfile, self).__init__(**kwargs)
        self.os_profile = os_profile
        self.storage_profile = storage_profile
        self.network_profile = network_profile
        self.diagnostics_profile = diagnostics_profile
        self.extension_profile = extension_profile
        self.license_type = license_type
