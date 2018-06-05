from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.ConfigurationApi(swagger_client.ApiClient())
cfg = swagger_client.NewConfiguration(name="GoogleSettings", value={"list" : 3}) # NewConfiguration | Configuration object to be added. Duplicates are allowed.

try:
    # Adds a new configuration
    api_response = api_instance.add_configuration(cfg)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->add_configuration: %s\n" % e)