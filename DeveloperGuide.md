
# Configuration Manager Developer Guide

This is the developer guide for a HTTP API for managing the configuration values of a system.

# TOC (Table of Content)

* [TOC](#TOC)
    - [Building dependencies](#building-dependencies)
    - [Building the web app](#building-the-web-app)
    - [Unit testing](#unit-testing)
    - [Running the web app](#running-the-web-app)
    - [Create an archive](#create-an-archive)
    - [Project Structure](#project-structure)

# Building Dependencies 

To build the web app you need the following software packages:

- `Python3`
- `Java 8`
- `maven`
- The latest version of `swagger-codegen` from this [repository](https://github.com/swagger-api/swagger-codegen)

Make sure each of those dependency has its path added to your `PATH` environment variable.

## Installation of dependencies on OSX

On OSX you can use the `brew` utility to install everything.
After you installed it (here there are some [instructions](https://brew.sh/)) you can type:

```
brew install python3
brew cask install homebrew/cask-versions/java8
brew install maven
brew install --HEAD swagger-codegen
```

## Other platforms

Other platforms are not supported yet.

# Building the web app

To build everything, if all the dependencies mentioned above are already satisfied, 
go to the main folder of the project and type:

```
./build_server.sh
```

Make sure that `./build_server.sh` has executable permissions.

It will create a directory called `build` inside the current folder structured like this:

    /app
    /docs

And will execute unit and functional testing.
If everything was good and no errors were reported, you are now ready to go and launch the web app.

# Unit testing

To launch only the unit test suite, go to the main folder of the project and type:

```
./unit_tests.sh
```

Please note that unit tests are automatically launched when building the web app.

# Running the web app

To launch the web app, please refer to [this section](Readme.md/#running-web-app).

# Create an archive

To create an archive that contains all the web server, go to the main folder of the project and type:
```
./create_archive.sh
```

An archive will be created inside the `deploy` folder called `configuration_manager.zip` with all you need
to kickstart you web app.

# Project 

## Folder Structure

This section is a stub.

## Preferred Editor

This section is a stub.

## Commit Legend

Commit Type | Emoji
----------  | -----
Initial Commit | [🎉 Party Popper](http://emojipedia.org/party-popper/)
Version Tag | [🔖 Bookmark](http://emojipedia.org/bookmark/)
New Feature | [✨ Sparkles](http://emojipedia.org/sparkles/)
Bugfix | [🐛 Bug](http://emojipedia.org/bug/)
Security Fix | [🔒 Lock](https://emojipedia.org/lock/)
Metadata | [📇 Card Index](http://emojipedia.org/card-index/)
Refactoring | [♻️ Black Universal Recycling Symbol](http://emojipedia.org/black-universal-recycling-symbol/)
Documentation | [📚 Books](http://emojipedia.org/books/)
Internationalization | [🌐 Globe With Meridians](http://emojipedia.org/globe-with-meridians/)
Accessibility | [♿ Wheelchair](https://emojipedia.org/wheelchair-symbol/)
Performance | [🐎 Horse](http://emojipedia.org/horse/)
Cosmetic | [🎨 Artist Palette](http://emojipedia.org/artist-palette/)
Tooling | [🔧 Wrench](http://emojipedia.org/wrench/)
Tests | [🚨 Police Cars Revolving Light](http://emojipedia.org/police-cars-revolving-light/)
Deprecation | [💩 Pile of Poo](http://emojipedia.org/pile-of-poo/)
Removal | [🗑️ Wastebasket](http://emojipedia.org/wastebasket/)
Work In Progress (WIP) | [🚧 Construction Sign](http://emojipedia.org/construction-sign/)
