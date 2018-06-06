#!/bin/sh

# You can pass this script the option "--no-cache" to create a new swagger server
cd build/app

# building the image
docker build $1 -t swagger_server .

# starting up a container
docker run -p 8080:8080 swagger_server
