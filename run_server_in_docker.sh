#!/bin/sh
# This script creates and launched a dockerized web app
# Must be launched from the main folder of the project
#
# You can pass this script the argument "--no-cache" to create a new server from scratch


cd build/app

# building the image
docker build $1 -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
