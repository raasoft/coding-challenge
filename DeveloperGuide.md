
# Configuration Manager Developer Guide

HTTP API for managing the configuration values of a system.

* [TOC](#TOC)
    - [Getting Started](#getting-started)
        - [Dependencies and Requirements](#dependencies-and-requirements)
        - [Installation](#Installation)
        - [Setting up the application](#setting-up-the-application)
    - [Usage](#usage)
    - [Developer Guide](#developer-guide)
## Dependencies and Requirements 

You need to install on your local machine:

- `python3`
- `pip3`
- `maven`
- The latest version of `swagger-codegen` from this [repository](https://github.com/swagger-api/swagger-codegen)
- `flask_cors`

Make sure each of those dependency has its path added to your `PATH` environment variable.

### Installation of dependencies on OSX

On OSX you can use the `brew` utility to install everything.
After you installed it (here there are some [instructions](https://brew.sh/)) you can type:

```
brew install python3
brew install maven
brew install --HEAD swagger-codegen
pip3 install flask_cors
```

### Linux, Windows

Those platform are not supported yet.

## Getting Started

To build everything and launch the webapp, go to the main folder of the project and type:

```
./build_server.sh
```

Make sure that `./build_server.sh` has executable permission.

It will create a directory called `build` inside the current folder structured like this:

    /app
    /docs

And will starts the application in development mode on `localhost:8080`.
Open your browser and navigate to http://localhost:8080 to see the application.
