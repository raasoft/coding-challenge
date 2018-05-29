#!/bin/sh
rm -r build

swagger-codegen generate -i src/api/swagger.yaml -l python-flask -o build/app
swagger-codegen generate -i src/api/swagger.yaml -l html -o build/docs
rm build/app/swagger_server/__main__.py
rm build/app/swagger_server/controllers/configuration_controller.py
cp src/app/swagger_server/__main__.py build/app/swagger_server
cp src/app/swagger_server/controllers/configuration_controller.py build/app/swagger_server/controllers/
cd build/app
python3 -m swagger_server