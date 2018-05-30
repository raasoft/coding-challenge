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

You need to install on your local machine:

- `python3` (with pip)
- `Java 8`
- `maven`
- The latest version of `swagger-codegen` from this [repository](https://github.com/swagger-api/swagger-codegen)

Make sure each of those dependency has its path added to your `PATH` environment variable.

### Installation of dependencies on OSX

On OSX you can use the `brew` utility to install everything.
After you installed it (here there are some [instructions](https://brew.sh/)) you can type:

```
brew install python3
brew cask install homebrew/cask-versions/java8
brew install maven
brew install --HEAD swagger-codegen
```

### Other platforms

Other platforms are not supported yet.


## Building the web app

To build everything, go to the main folder of the project and type:

```
./build_server.sh
```

Make sure that `./build_server.sh` has executable permission.

It will create a directory called `build` inside the current folder structured like this:

    /app
    /docs

And will execute unit and functional testing.
If everything was good and no errors were reported, you are now ready to go and launch the web app.

## Running the web app

To launch the we bapp, go to the main folder of the project and type:

```
./run_server.sh
```

Make sure that `./run_server.sh` has executable permission as well.

The application will start in development mode on `localhost:8080`.
If you open your browser and navigate to http://localhost:8080/v1/ui/ you can interact with it with a custom ui app to test the web app manually.

## Developer Guide

Please refer to [Developer Guide](./DeveloperGuide.md)