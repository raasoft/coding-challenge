#!/bin/sh
# This script runs the web application.
# Needs to be launched by the main folder of the project

cd build/app

pip3 install -r requirements.txt --force-reinstall
python3 -m swagger_server $1