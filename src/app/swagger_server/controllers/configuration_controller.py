import connexion
import six

from swagger_server.models.configuration import Configuration  # noqa: E501
from swagger_server.models.new_configuration import NewConfiguration  # noqa: E501
from swagger_server import util
from flask import abort

from flask import make_response
from flask import Response
from swagger_server.controllers.fake_database import FakeDatabase
import json
import uuid
import base64


def get_a_uuid():
    u = uuid.uuid4()
    return str(u)

def add_configuration(configuration):  # noqa: E501
    """Adds a new configuration

     # noqa: E501

    :param configuration: Configuration object to be added. Duplicates are allowed.
    :type configuration: dict | bytes

    :rtype: Configuration
    """
    if connexion.request.is_json:
        configuration = NewConfiguration.from_dict(connexion.request.get_json())  # noqa: E501

        configurationObj = Configuration(get_a_uuid(), configuration.name, configuration.value )

        # newConfDict = {'name':configurationObj.name, 'value':configurationObj.value, 'id':configurationObj.uuid }
        # newConf = json.dumps(newConfDict)

        db = FakeDatabase.getInstance()
        db.save(configurationObj.id, configurationObj)

        return configurationObj

    return 505

def delete_configuration(id):  # noqa: E501
    """Deletes a Configuration

     # noqa: E501

    :param id: Configuration id to delete
    :type id: 

    :rtype: None
    """
    db = FakeDatabase.getInstance()
    db.remove(id)


def find_configuration_by_name(name):  # noqa: E501
    """Finds configuration by name

    Only one name must be provided. # noqa: E501

    :param name: Name to be searched in configurations
    :type name: str

    :rtype: List[Configuration]
    """

    db = FakeDatabase.getInstance()
    resultList = []

    for obj in db.search(name):
        resutlList.append(Configuration.from_dict(obj))
    
    return resultList


def get_configuration_by_id(id):  # noqa: E501
    """Finds configuration by ID

    Returns a single configuration # noqa: E501

    :param id: ID of configuration to return
    :type id: 

    :rtype: Configuration
    """

    db = FakeDatabase.getInstance()

    try:
        return db.read(id)
    except Exception as e:
        text = '{ \
        "detail": "Configuration with id ' + str(id) + ' not found", \
        "status": 404, \
        "title": "Not Found", \
        "type": "about:blank" }' 

        resp = make_response(text, 404)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['content-type'] = 'application/problem+json'

        return resp


def update_configuration(configuration):  # noqa: E501
    """Updates an existing configuration

     # noqa: E501

    :param configuration: Configuration object that needs to be updated
    :type configuration: dict | bytes

    :rtype: Configuration
    """
    if connexion.request.is_json:
        configuration = Configuration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic POR FAVOR!'
