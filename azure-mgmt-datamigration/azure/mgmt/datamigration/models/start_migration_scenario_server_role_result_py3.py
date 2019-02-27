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


class StartMigrationScenarioServerRoleResult(Model):
    """Server role migration result.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Name of server role.
    :vartype name: str
    :ivar state: Current state of migration. Possible values include: 'None',
     'InProgress', 'Failed', 'Warning', 'Completed', 'Skipped', 'Stopped'
    :vartype state: str or ~azure.mgmt.datamigration.models.MigrationState
    :ivar exceptions_and_warnings: Migration exceptions and warnings.
    :vartype exceptions_and_warnings:
     list[~azure.mgmt.datamigration.models.ReportableException]
    """

    _validation = {
        'name': {'readonly': True},
        'state': {'readonly': True},
        'exceptions_and_warnings': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'exceptions_and_warnings': {'key': 'exceptionsAndWarnings', 'type': '[ReportableException]'},
    }

    def __init__(self, **kwargs) -> None:
        super(StartMigrationScenarioServerRoleResult, self).__init__(**kwargs)
        self.name = None
        self.state = None
        self.exceptions_and_warnings = None
