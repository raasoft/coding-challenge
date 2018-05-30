import logging

import connexion
from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder

from flask_injector import FlaskInjector

from swagger_server.controllers.fake_database import FakeDatabase
from injector import Binder


def configure(binder: Binder) -> Binder:
    binder.bind(
        FakeDatabase,
        FakeDatabase.getInstance()
    )

class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')

        FlaskInjector(app=app.app, modules=[configure])

        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app.app
