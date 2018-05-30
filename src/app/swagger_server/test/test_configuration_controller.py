# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.configuration import Configuration  # noqa: E501
from swagger_server.models.new_configuration import NewConfiguration  # noqa: E501
from swagger_server.test import BaseTestCase

from flask_injector import inject
from injector import Module, with_injector, inject

from swagger_server.controllers.fake_database import FakeDatabase

sampleValue = { "name" : "GoogleSettings", "value" : {"list" : 3}}
sampleValue2 = { "name" : "HaikySettings", "value" : {"tea" : 66}}
newConfiguration = NewConfiguration.from_dict(sampleValue)    
sampleNewConfiguration2 = NewConfiguration.from_dict(sampleValue2) 

sampleConfiguration = Configuration("2e094f21-7a6f-4268-b1ff-c2a376de35ad", newConfiguration.name, newConfiguration.value )

class TestDbModule(Module):

    def configure(self, binder):

        testDb = dict()
        testDb[sampleConfiguration.id] = sampleConfiguration

        db = FakeDatabase.getInstance()
        db.load(testDb)

        binder.bind(FakeDatabase, db)

class TestConfigurationController(BaseTestCase):
    """ConfigurationController integration test stubs"""

    def test_add_configuration(self):
        """Test case for add_configuration

        Adds a new configuration
        """
        configuration = sampleConfiguration 

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
            '/v1/configuration/{id}'.format(id=sampleConfiguration.id),
            method='DELETE')
        self.assertEqual(response.status_code, 204, 
            'Response body is : ' + response.data.decode('utf-8'))

    @with_injector(TestDbModule())
    @inject
    def test_find_configuration_by_name(self):
        """Test case for find_configuration_by_name

        Finds configuration by name
        """
        query_string = [('name', sampleConfiguration.name)]
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
            '/v1/configuration/{id}'.format(id=sampleConfiguration.id),
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
        configuration = Configuration(sampleConfiguration.id, sampleNewConfiguration2.name, sampleNewConfiguration2.value)
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
