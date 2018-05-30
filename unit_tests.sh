#!/bin/sh
cd build/app

pip3 install -r requirements.txt
tox -e py36

