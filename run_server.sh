#!/bin/sh
cd build/app

if [ $1 = "--docker" ]; then
    docker build -t swagger_server .
    docker run -p 8080:8080 swagger_server
else
    pip3 install -r requirements.txt --force-reinstall
    python3 -m swagger_server
fi

