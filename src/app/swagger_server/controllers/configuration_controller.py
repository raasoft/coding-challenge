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




def add_configuration(configuration):  # noqa: E501
    """Adds a new configuration

     # noqa: E501

    :param configuration: Configuration object to be added. Duplicates are allowed.
    :type configuration: dict | bytes

    :rtype: Configuration
    """
    if connexion.request.is_json:
        db = FakeDatabase.getInstance()

        configuration = NewConfiguration.from_dict(connexion.request.get_json())  # noqa: E501
        configurationObj = Configuration(db.get_a_uuid(), configuration.name, configuration.value )

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

    try:
        db.remove(id)
        
        return ('', 204)

    except KeyError as e:
        
        text = '{ \
        "detail": "Configuration with id ' + str(id) + ' not found", \
        "status": 404, \
        "title": "Not Found", \
        "type": "about:blank" }' 

        resp = make_response(text, 404)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['content-type'] = 'application/problem+json'

        return resp

    abort(500)


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
        resultList.append(obj)

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
    except KeyError as e:
        
        text = '{ \
        "detail": "Configuration with id ' + str(id) + ' not found", \
        "status": 404, \
        "title": "Not Found", \
        "type": "about:blank" }' 

        resp = make_response(text, 404)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['content-type'] = 'application/problem+json'

        return resp

    except ValueError as e:
        text = '{ \
        "detail": "Configuration id ' + str(id) + ' is not a valid uuid", \
        "status": 400, \
        "title": "Not Found", \
        "type": "about:blank" }' 

        resp = make_response(text, 400)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['content-type'] = 'application/problem+json'

        return resp

    abort(500)

def update_configuration(configuration):  # noqa: E501
    """Updates an existing configuration

     # noqa: E501

    :param configuration: Configuration object that needs to be updated
    :type configuration: dict | bytes

    :rtype: Configuration
    """
    if connexion.request.is_json:
        configuration = Configuration.from_dict(connexion.request.get_json())  # noqa: E501
        
        try:
            db = FakeDatabase.getInstance()
            obj = db.read(configuration.id)

            obj.name = configuration.name
            obj.value = configuration.value

            db.save(configuration.id, configuration)

            return obj

        except KeyError as e:
        
            text = '{ \
            "detail": "Configuration with id ' + str(configuration.id) + ' not found", \
            "status": 404, \
            "title": "Not Found", \
            "type": "about:blank" }' 

            resp = make_response(text, 404)
            resp.headers['Access-Control-Allow-Origin'] = '*'
            resp.headers['content-type'] = 'application/problem+json'

            return resp

        abort(500)