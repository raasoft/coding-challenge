#!/bin/sh
cd build/app

pip3 install -r requirements.txt --force-reinstall
python3 -m swagger_server $1