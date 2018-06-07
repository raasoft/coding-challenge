# System Configuration Manager

[![Build Status](https://travis-ci.org/raasoft/coding-challenge.svg?branch=master)](https://travis-ci.org/raasoft/coding-challenge)
[![codecov](https://codecov.io/gh/raasoft/coding-challenge/branch/master/graph/badge.svg)](https://codecov.io/gh/raasoft/coding-challenge)
[![GitHub contributors](https://img.shields.io/github/contributors/raasoft/coding-challenge.svg)](https://github.com/raasoft/coding-challenge/graphs/contributors)

HTTP API for managing the configuration values of a system.

# TOC (Table of Content)

* [TOC](#TOC)
    - [Dependencies and Requirements](#dependencies-and-requirements)
    - [Running the web app](#running-the-web-app)
        - [Testing the web app endpoints](#Testing-the-web-app-endpoints)
            - [Manual testing via Web UI](#manual-testing-via-web-ui)
            - [Validation testing](#validation-testing)
    - [API Documentation](#api-documentation)
    - [Troubleshooting](#troubleshooting)
    - [Developer Guide](#developer-guide)

## Dependencies and Requirements 

To launch the web app you need to install on your local machine:

- `python3` (with pip)

## Running the web app

If you don't already have a release of the web app, _you need to build it first_.

**To build the web app**, follow [this section](#DeveloperGuide.md) of `DeveloperGuide.md` document, then continue reading here.

To launch the web app, go to the main folder of the project release and type:

```bash
./run_server.sh
```

Make sure that `./run_server.sh` has executable permission as well.

The application will start on [http://localhost:8080/](http://localhost:8080/).

##### Running the web app in Docker

If you use Docker, you can run the web app using docker by issuing:

```bash
./run_server_in_docker.sh
```
The docker container will expose the application on [http://localhost:8080/](http://localhost:8080/).

## Testing the web app endpoints


### Manual testing via Web UI

If you open your browser and navigate to [http://localhost:8080/v1/ui/](http://localhost:8080/v1/ui/) you can interact with it with a custom ui app to test the web app manually.

### Validation Testing

If you want to execute **unit tests** or **validation tests**, you need to setup a full development environment where to launch validation tests, by cloning [the project repository](https://github.com/raasoft/coding-challenge.git) and then reading [this section](DeveloperGuide.md#validation-testing) of the `DeveloperGuide.md` document.


# API Documentation

If you don't already have a release of the web app, **you need to build it first** to generate documentations.
Follow [this section](#DeveloperGuide.md) to build it, then you will find API specifications in HTML format in `build/docs/index.html`.

# Troubleshooting

## OSError: [Errno 48] Address already in use

If this error is shown after the web server has started, it means that there is already a service listening at the address and port used.

At this stage, the address used by the web server is fixed and cannot be changed, so the only way to get rid of this is to shutdown other services using the same address and retry.

In future releases we are going to let the user decide a custom address.

# Developer Guide

Please refer to [Developer Guide](./DeveloperGuide.md) to know how to contribute to this project and to know how to perform validation testing.