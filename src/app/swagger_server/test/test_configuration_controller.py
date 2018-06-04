# coding: utf-8

from __future__ import absolute_import

from flask import json

from injector import Module, with_injector, inject

from swagger_server.models.configuration import Configuration
from swagger_server.models.new_configuration import NewConfiguration
from swagger_server.test import BaseTestCase


from swagger_server.controllers.fake_database import FakeDatabase

### Those values are used in unit testing #####################################

UNIT_TEST_SAMPLE_VALUE = {"name" : "GoogleSettings", "value" : {"list" : 3}}
UNIT_TEST_SAMPLE_VALUE_2 = {"name" : "HaikySettings", "value" : {"tea" : 66}}
UNIT_TEST_SAMPLE_NEW_CFG = NewConfiguration.from_dict(UNIT_TEST_SAMPLE_VALUE)
UNIT_TEST_SAMPLE_NEW_CFG2 = NewConfiguration.from_dict(UNIT_TEST_SAMPLE_VALUE_2)

UNIT_TEST_SAMPLE_CFG = Configuration("2e094f21-7a6f-4268-b1ff-c2a376de35ad",
                                     UNIT_TEST_SAMPLE_NEW_CFG.name,
                                     UNIT_TEST_SAMPLE_NEW_CFG.value)

###############################################################################
class TestDbModule(Module):

    def configure(self, binder):

        sample_database = dict()
        sample_database[UNIT_TEST_SAMPLE_CFG.id] = UNIT_TEST_SAMPLE_CFG

        unit_test_database = FakeDatabase.getInstance()
        unit_test_database.load(sample_database)

        binder.bind(FakeDatabase, unit_test_database)

class TestConfigurationController(BaseTestCase):
    """ConfigurationController integration test stubs"""

    def test_add_configuration(self):
        """Test case for add_configuration

        Adds a new configuration
        """
        configuration = UNIT_TEST_SAMPLE_CFG

        response = self.client.open(
            '/v1/configuration',
            method='POST',
            data=json.dumps(configuration),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @with_injector(TestDbModule())
    @inject
    def test_delete_configuration(self, data_provider: FakeDatabase):
        """Test case for delete_configuration

        Deletes a Configuration
        """

        response = self.client.open(
            '/v1/configuration/{id}'.format(id=UNIT_TEST_SAMPLE_CFG.id),
            method='DELETE')
        self.assertEqual(response.status_code, 204,
                         'Response body is : ' + response.data.decode('utf-8'))

    @with_injector(TestDbModule())
    @inject
    def test_find_configuration_by_name(self):
        """Test case for find_configuration_by_name

        Finds configuration by name
        """
        query_string = [('name', UNIT_TEST_SAMPLE_CFG.name)]
        response = self.client.open(
            '/v1/configuration/findByName',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @with_injector(TestDbModule())
    @inject
    def test_find_configuration_by_name_no_results(self):
        """Test case for find_configuration_by_name

        Finds configuration by name
        """
        query_string = [('name', "StrangeNameNeverInserted")]
        response = self.client.open(
            '/v1/configuration/findByName',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @with_injector(TestDbModule())
    @inject
    def test_get_configuration_by_id(self):
        """Test case for get_configuration_by_id

        Finds configuration by ID
        """
        response = self.client.open(
            '/v1/configuration/{id}'.format(id=UNIT_TEST_SAMPLE_CFG.id),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_configuration_by_id_with_not_uuid_id(self):
        """Test case for get_configuration_by_id_with_not_uuid_id

        Finds configuration by ID but should fail since ID is malformed
        returning an Error 400
        """
        response = self.client.open(
            '/v1/configuration/{id}'.format(id="clearly_malformed_uuid"),
            method='GET')
        self.assertEqual(response.status_code, 400,
                         'Response body is : ' + response.data.decode('utf-8'))

    @with_injector(TestDbModule())
    @inject
    def test_update_configuration(self):
        """Test case for update_configuration

        Updates an existing configuration
        """
        configuration = Configuration(UNIT_TEST_SAMPLE_CFG.id,
                                      UNIT_TEST_SAMPLE_NEW_CFG2.name,
                                      UNIT_TEST_SAMPLE_NEW_CFG2.value)
        response = self.client.open(
            '/v1/configuration',
            method='PUT',
            data=json.dumps(configuration),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))



if __name__ == '__main__':
    import unittest
    unittest.main()
