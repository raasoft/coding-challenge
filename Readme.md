# System Configuration Manager

HTTP API for managing the configuration values of a system.

# TOC (Table of Content)

* [TOC](#TOC)
    - [Dependencies and Requirements](#dependencies-and-requirements)
        - [Installation of dependencies on OSX](#installation-of-dependencies-on-osx)
        - [Other Platforms](#other-platforms)
    - [Building the web app](#building-the-web-app)
    - [Running the web app](#running-the-web-app)
    - [Developer Guide](#developer-guide)

## Dependencies and Requirements 

To launch the web app you need to install on your local machine:

- `python3` (with pip)

## Running the web app

If you don't already have a release of the web app, you need to build it first.
Follow [this section](DeveloperGuide.md#) to build it first, then continue reading here.

To launch the web app, go to the main folder of the project and type:

```
./run_server.sh
```

Make sure that `./run_server.sh` has executable permission as well.

The application will start in development mode on `localhost:8080`.
If you open your browser and navigate to http://localhost:8080/v1/ui/ you can interact with it with a custom ui app to test the web app manually.

## Developer Guide

Please refer to [Developer Guide](./DeveloperGuide.md)