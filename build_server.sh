#!/bin/sh
rm -r build

swagger-codegen generate -i src/api/swagger.yaml -l python-flask -o build/app
swagger-codegen generate -i src/api/swagger.yaml -l html -o build/docs

rm build/app/requirements.txt
cp src/app/requirements.txt build/app

rm build/app/test-requirements.txt
cp src/app/test-requirements.txt build/app

rm build/app/swagger_server/__main__.py
cp src/app/swagger_server/__main__.py build/app/swagger_server

rm build/app/swagger_server/controllers/configuration_controller.py
cp src/app/swagger_server/controllers/configuration_controller.py build/app/swagger_server/controllers/

rm build/app/swagger_server/test/__init__.py
cp src/app/swagger_server/test/__init__.py build/app/swagger_server/test/

rm build/app/swagger_server/test/test_configuration_controller.py
cp src/app/swagger_server/test/test_configuration_controller.py build/app/swagger_server/test/

rm build/app/swagger_server/controllers/fake_database.py
cp src/app/swagger_server/controllers/fake_database.py build/app/swagger_server/controllers/
cd build/app

pip3 install -r requirements.txt
tox -e py36

