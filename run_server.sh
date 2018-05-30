#!/bin/sh
cd build/app
pip3 install -r requirements.txt
python3 -m swagger_server
