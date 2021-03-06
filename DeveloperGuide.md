
# Configuration Manager Developer Guide

This is the developer guide for a HTTP API for managing the configuration values of a system.

# TOC (Table of Content)

* [TOC](#TOC)
    - [Getting started](#getting-started)
        - [Installing dependencies](#installing-dependencies)
        - [Building the web app](#building-the-web-app)
        - [Running the web app](#running-the-web-app)
        - [Testing](#testing)
            - [Unit testing](#unit-testing)
            - [Validation testing](#validation-testing)
        - [Make a release](#make-a-release)
    - [Project Overview](#project-overview)
        - [Folder Structure](#folder-structure)

# Getting Started

In this section are presented the main operations that a developer would do while 
developing this app.

For a broader overview about project structure, visit [this section](#project-overview).

## Installing Dependencies 

To build the web app you need the following software packages:

- `Python3`
- The latest version of `swagger-codegen` from this [repository](https://github.com/swagger-api/swagger-codegen)
    - `Java 8` (needed by swagger-codegen)
    - `maven` (needed by swagger-codegen)

Make sure each of those dependency has its path added to your `PATH` environment variable.

### Installation of dependencies on OSX

On OSX you can use the `brew` utility to install everything.
After you installed it (here there are some [instructions](https://brew.sh/)) you can type (from the main directory of this repository):

```
brew install python3
pip3 install -r src/app/requirements.txt
brew cask install homebrew/cask-versions/java8
brew install --HEAD swagger-codegen
```

### Other platforms

Other platforms are not supported yet.

## Building the web app

To build everything, if all the dependencies mentioned above are already satisfied, 
go to the main folder of the project and type:

```bash
invoke build
```

It will create a directory called `build` inside the current folder structured like this:

    /app
    /docs

And will execute unit testing.
If everything run smoothly and no errors were reported, you are now ready to go and [launch the web app](#running-the-web-app).

## Running the web app

As a developer, to launch the web app, you have two options:
- Launch it in a user-fashion way 
- Use the same semantic used for building the app (recommended for a developer)

If you want to run it in a user-fashion way, please refer to [this section](Readme.md/#running-web-app).

Otherwise, you just issue (from the main folder):

```bash
invoke run
```

If you are a developer you will find this way much more convenient.

If you want to build & run the application with a single command, just issue:

```bash
invoke run --rebuild
```

If you want to run it in a dockerized enviroment, use:

```bash
invoke run --docker
```

## Make a release

To create a release that contains all the web server, go to the main folder of the project and type:
```
invoke release
```

A zip archive will be created inside the `release` folder with all you need
to kickstart you web app.

## Testing

Here you will find how to launch unit, integration and validation testing.

To know how to edit existing tests, please refer to [this section](#folder-structure) 
and search for the files related to testing.

### Unit Testing

To launch only the unit test suite, go to the main folder of the project and type:

```bash
invoke unittest
```

Please note that unit tests are automatically launched when building the web app.
The unit testing framework used in this project is `nose` with `tox`.

If you need to modify tox settings, edit `src/app/tox.ini`.

### Validation Testing

To launch only the validation test suite, go to the main folder of the project and type:

```bash
invoke validate
```

Please note that the **web server must be already running** (validation test does not start it).
To launch it, please see [this section](#running-the-web-app).

# Project Overview

The project is build by two fundamental parts:

- Business logic (contained in `src/app`)
- Boilerplate code (autogenerated in `build` folder from the OpenAPI specifications `src/api/swagger.yaml`)

All the boilerplate code is NOT versioned (you won't find it in a newly cloned repo) and generated only when a new build [is issued](#Building-the-web-app).

## Build manager

The build manager used in this project is `pyinvoke`.
We choose this because it is clean and simple.

To have a list of all the most common build targets, issue:

```bash
invoke help
```

To have a list of all the possible build targets, issue:

```bash
invoke --list
```

You can find more information about this file inside the [folder structure](#folder-structure) section.

## Folder Structure

#### <kbd>src</kbd> folder

A newly cloned repo comes with a directory called `src`.

Inside this folder, is contained all the business-logic dependent files that needs to be
created, modified, according to the software internal behaviour.

Once the build procedure is issued, after the boilerplate code has been generated, 
files in this folder are substituted to the boilerplate ones to implement the feature requested.

Each relevant file is documented with some inline comments to get you started. 
Here we’ll go through the main ones.

##### <kbd>api/swagger.yaml</kbd> source file

This is the OpenAPI specification. From this file, **all the boilerplate code** is generated.

##### <kbd>app/swagger_server/controllers/configuration_controller.py</kbd> source file

This file contains the business logic of the whole project: all the REST endpoints
controllers lie here.

If you want to edit a particular API behaviour, **this is the main file to edit**.

##### <kbd>app/swagger_server/test/test_configuration_controller.py</kbd> source file

This file contains the unit and integration test for the whole project.
If you want to add/edit/delete a unit test, this is the main file to edit.

Inside this file, **dependency injection** was used to inject a fake database for the tests.

The only requirement to add a test in an existing class, is that the test 
method must start with the prefix `test_`.

To create a new class, just copy an existing class file and rename it (maintaining it 
in the same folder), both class name and file name.

##### <kbd>app/swagger_server/func_test/test/test_configuration_api.py</kbd> source file

This file contains the validation tests for the whole project (e.g. a particular API needs
to answer in no more than 200 ms).
If you want to add/edit/delete a validation test, this is the main file to edit.

The only requirement to add a test in an existing class, is that the test 
method must start with the prefix `test_`.

To create a new class, just copy an existing class file and rename it (maintaining it 
in the same folder), both class name and file name.

##### <kbd>tasks.py</kbd> source file

This file contains all the targets that the `invoke` build manager is able to execute.
To create a new task, just declare a new method with the `@task` decorator, and be sure
that this function has at least one argument, the `ctx` (contest) argument.

For more information, please see the original [pyinvoke documentation](http://www.pyinvoke.org/)

## Linting

A Lint or a Linter is a program that supports linting (verifying code quality). 
They are available for most languages like JavaScript, CSS, HTML, Python, etc..
In this project, we use the same linting guidelines that Google Chrome uses for python projects.

The linter file is `.pylintrc`.

## Preferred Editor

You can open this project with other editors or IDEs, but the preferred editor 
to develop this project is Visual Studio Code: you can open the workspace 
`CodingChallenge.code-workspace` to start working with it!

We choose Visual Studio Code because it has nice built-in features like:
- Automatic Python Linting 
- Embedded git version control (via [Gitlens](vscode:extension/eamodio.gitlens))

## Commit Legend

In this project, we try to put an expressive emoji at the begin of each commit.

Using emojis on commit messages provides an easy way of identifying the 
purpose or intention of a commit with only looking at the emojis used 
(and moreover, it's fun!). 


Commit Type | Emoji
----------  | -----
Initial Commit  | [🎉 Party Popper](http://emojipedia.org/party-popper/)
Version Tag     | [🔖 Bookmark](http://emojipedia.org/bookmark/)
New Feature     | [✨ Sparkles](http://emojipedia.org/sparkles/)
Bugfix          | [🐛 Bug](http://emojipedia.org/bug/)
Security Fix    | [🔒 Lock](https://emojipedia.org/lock/)
Metadata        | [📇 Card Index](http://emojipedia.org/card-index/)
Refactoring     | [♻️ Black Universal Recycling Symbol](http://emojipedia.org/black-universal-recycling-symbol/)
Documentation   | [📚 Books](http://emojipedia.org/books/)
Internationalization | [🌐 Globe With Meridians](http://emojipedia.org/globe-with-meridians/)
Accessibility   | [♿ Wheelchair](https://emojipedia.org/wheelchair-symbol/)
Performance     | [🐎 Horse](http://emojipedia.org/horse/)
Cosmetic        | [🎨 Artist Palette](http://emojipedia.org/artist-palette/)
Tooling         | [🔧 Wrench](http://emojipedia.org/wrench/)
Tests           | [🚨 Police Cars Revolving Light](http://emojipedia.org/police-cars-revolving-light/)
Deprecation     | [💩 Pile of Poo](http://emojipedia.org/pile-of-poo/)
Removal         | [🗑️ Wastebasket](http://emojipedia.org/wastebasket/)
Work In Progress (WIP) | [🚧 Construction Sign](http://emojipedia.org/construction-sign/)

### Using Emoji is Hard! 😡

Here are some ways to more easily integrate emoji into your workflow.

#### OSX Emojis

You can pull up the emoji keyboard by hitting <kbd>ctrl</kbd>+<kbd>⌘</kbd>+<kbd>space</kbd>