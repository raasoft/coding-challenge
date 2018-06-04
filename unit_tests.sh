#!/bin/sh
cd build/app

pip3 install -r requirements.txt --force-reinstall
tox -e py36

