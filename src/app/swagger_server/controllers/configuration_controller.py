import connexion
import six

from swagger_server.models.configuration import Configuration  # noqa: E501
from swagger_server.models.new_configuration import NewConfiguration  # noqa: E501
from swagger_server import util


def add_configuration(configuration):  # noqa: E501
    """Adds a new configuration

     # noqa: E501

    :param configuration: Configuration object to be added. Duplicates are allowed.
    :type configuration: dict | bytes

    :rtype: Configuration
    """
    if connexion.request.is_json:
        configuration = NewConfiguration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic POR FAVOR!'


def delete_configuration(id):  # noqa: E501
    """Deletes a Configuration

     # noqa: E501

    :param id: Configuration id to delete
    :type id: 

    :rtype: None
    """
    return 'do some magic POR FAVOR!'


def find_configuration_by_name(name):  # noqa: E501
    """Finds configuration by name

    Only one name must be provided. # noqa: E501

    :param name: Name to be searched in configurations
    :type name: str

    :rtype: List[Configuration]
    """
    return 'do some magic POR FAVOR!'


def get_configuration_by_id(id):  # noqa: E501
    """Finds configuration by ID

    Returns a single configuration # noqa: E501

    :param id: ID of configuration to return
    :type id: 

    :rtype: Configuration
    """
    return 'do some magic POR FAVOR!'


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
