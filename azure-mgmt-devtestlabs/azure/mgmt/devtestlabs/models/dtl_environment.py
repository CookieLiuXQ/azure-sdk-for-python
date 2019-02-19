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

from .resource import Resource


class DtlEnvironment(Resource):
    """An environment, which is essentially an ARM template deployment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The identifier of the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: The location of the resource.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :param deployment_properties: The deployment properties of the
     environment.
    :type deployment_properties:
     ~azure.mgmt.devtestlabs.models.EnvironmentDeploymentProperties
    :param arm_template_display_name: The display name of the Azure Resource
     Manager template that produced the environment.
    :type arm_template_display_name: str
    :ivar resource_group_id: The identifier of the resource group containing
     the environment's resources.
    :vartype resource_group_id: str
    :ivar created_by_user: The creator of the environment.
    :vartype created_by_user: str
    :ivar provisioning_state: The provisioning status of the resource.
    :vartype provisioning_state: str
    :ivar unique_identifier: The unique immutable identifier of a resource
     (Guid).
    :vartype unique_identifier: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'resource_group_id': {'readonly': True},
        'created_by_user': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'unique_identifier': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'deployment_properties': {'key': 'properties.deploymentProperties', 'type': 'EnvironmentDeploymentProperties'},
        'arm_template_display_name': {'key': 'properties.armTemplateDisplayName', 'type': 'str'},
        'resource_group_id': {'key': 'properties.resourceGroupId', 'type': 'str'},
        'created_by_user': {'key': 'properties.createdByUser', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'unique_identifier': {'key': 'properties.uniqueIdentifier', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DtlEnvironment, self).__init__(**kwargs)
        self.deployment_properties = kwargs.get('deployment_properties', None)
        self.arm_template_display_name = kwargs.get('arm_template_display_name', None)
        self.resource_group_id = None
        self.created_by_user = None
        self.provisioning_state = None
        self.unique_identifier = None
