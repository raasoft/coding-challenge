from invoke import task
import shutil
import os
import sys


SRC_BASE_PATH = "src/app/"
BUILD_BASE_PATH = "build/app/"
RELEASE_FOLDER = "release"

VALIDATION_BUILD_BASE_PATH = "build/validate/swagger_client/"
VALIDATION_SRC_BASE_PATH = "src/app/swagger_server/func_test/"

ARCHIVE_FILENAME = "configuration_manager"

SRC_FILES = ["requirements.txt",
             "test-requirements.txt",

             "swagger_server/config.py",

             "swagger_server/__main__.py",
             "swagger_server/controllers/configuration_controller.py",

             "swagger_server/test/__init__.py",
             "swagger_server/test/test_configuration_controller.py",

             "swagger_server/controllers/fake_database.py",

             "swagger_server/controllers/fake_database.py",

             "tox.ini",

             "Dockerfile"

            ]

FUNC_TEST_FILES = ["main.py",
                   "tox.ini",
                   "README.md",
                   "test/test_configuration_api.py",

                  ]

RELEASE_FILES = ["build/app",
                 "build/docs",

                 "run_server.sh",
                 "run_server_in_docker.sh",

                 "Readme.md",
                 "DeveloperGuide.md"
                ]

@task
def splash(ctx):
    """ Shows the splash screen """
    print("\n\n✨✨✨ Coding Challenge web app")

@task
def clean(ctx):
    """🗑  Clean target for the project """

    print("\n🗑  Cleaning the build directory...")
    try:
        shutil.rmtree("build", ignore_errors=True)
    except Exception as excp:
        print("...with an error! 😡")
        print(excp)
        sys.exit(-1)

    print("...successfully! ✅")

@task(clean)
def generate(ctx):
    """ Generate source code for the project. Used by build target. """
    print("\n🔧 Generating code from APIs...\n")

    try:

        print("Generating code from APIs...")
        cmd = ("swagger-codegen generate -i src/api/swagger.yaml"
               " -l python-flask -o build/app"
              )

        result = ctx.run(cmd, hide=True, warn=True)
        if not result.ok:
            raise Exception("Cannot run code generation from API")

        print("Generating docs from APIs...")
        cmd = ("swagger-codegen generate -i src/api/swagger.yaml"
               " -l html -o build/docs"
              )
        result = ctx.run(cmd, hide=True, warn=True)
        if not result.ok:
            raise Exception("Cannot run docs generation from API")

        print("Updating web app files with updated business logic...")
        for src_file in SRC_FILES:
            try:
                os.remove(BUILD_BASE_PATH+src_file)
            except OSError as excp:
                if excp.errno != 2:
                    raise excp

            shutil.copy(SRC_BASE_PATH + src_file,
                        BUILD_BASE_PATH + src_file)

    except Exception as excp:
        print("...with an error! 😡")
        print(excp)
        sys.exit(-1)

    print("...successfully! ✅")

@task(generate)
def unittest(ctx):
    """ Build the target and launches unit tests"""
    print("\n🚨 Launching unit tests...\n")

    try:

        os.chdir("build/app")
        cmd = 'pip3 install -r requirements.txt'
        result = ctx.run(cmd, hide=False, warn=True)
        if not result.ok:
            print("...with an error! 😡")

        cmd = 'tox -e py36'
        result = ctx.run(cmd, hide=False, warn=True)
        if not result.ok:
            raise Exception("Error during runnig `tox` for unit testing")

        os.chdir("../..")

    except Exception as excp:
        print("...with an error! 😡")
        print(excp)
        sys.exit(-1)

    print("\n...successfully! ✅\n")
    print("📒  You can find a report at " + BUILD_BASE_PATH + "nosetests.xml")


@task(splash, generate, unittest)
def build(ctx):
    """ 🔧 Builds the whole project """
    print("\n🎉🎉🎉 Coding Challenge app built with success!\n")
    print("Run `./run_server.sh` to launch the web app")


def launch_validation_testing(ctx):
    """ Generate validation testing client and then launchs it """
    try:
        print("Generating validation testing from APIs...")
        cmd = ("swagger-codegen generate -i src/api/swagger.yaml"
               " -l python -o " + VALIDATION_BUILD_BASE_PATH
              )

        result = ctx.run(cmd, hide=True, warn=True)
        if not result.ok:
            raise Exception("Cannot run code generation from API")

        print("Updating functional testing files "
              "with updated business logic...")
        for functestfile in FUNC_TEST_FILES:
            try:
                os.remove(VALIDATION_BUILD_BASE_PATH + functestfile)
            except OSError as excp:
                if excp.errno != 2:
                    raise excp

            shutil.copy(VALIDATION_SRC_BASE_PATH + functestfile,
                        VALIDATION_BUILD_BASE_PATH + functestfile)

        os.chdir(VALIDATION_BUILD_BASE_PATH)
        cmd = 'tox -e py36'
        result = ctx.run(cmd, hide=False, warn=True)
        if not result.ok:
            raise Exception("Error during functional testing!")

        os.chdir("../..")
        return True

    except Exception as excp:
        print("...with an error! 😡")
        print(excp)
        sys.exit(-1)

@task(splash)
def validate(ctx):
    """ 🚨  Launches validation testing (web server must be already running) """
    print("\n🚨 Launching functional tests...\n")

    launch_validation_testing(ctx)

    print("...successfully! ✅\n")
    print("📒  You can find a report at " +
          VALIDATION_BUILD_BASE_PATH + "nosetests.xml")

@task(build)
def release(ctx):
    """ 📦  Creates a release creating an archive containing the whole app """

    print("\n📦 Creating compressed file archive in `" +
          RELEASE_FOLDER + "` folder...")

    try:
        result = shutil.rmtree(RELEASE_FOLDER, ignore_errors=True)

        os.makedirs(RELEASE_FOLDER)

        files_to_compress = ' '.join(RELEASE_FILES)

        cmd = ('zip -q -r '+RELEASE_FOLDER+'/'+ ARCHIVE_FILENAME +'.zip '
               "" + files_to_compress)
        result = ctx.run(cmd, hide=False, warn=True)
        if not result.ok:
            raise Exception("Cannot create zip file")

    except Exception as excp:
        print("...with an error! 😡")
        print(excp)
        sys.exit(-1)

    print("...successfully! ✅")
    print("\n🎉🎉🎉 Coding Challenge app " + ARCHIVE_FILENAME +
          " created with success!\n")

@task(splash)
def help(ctx):
    """ 🚑  Shows help menu """
    print("")
    print("🚚 Enter: 'invoke run --rebuild' to build and run the web server")
    print("🚨 Enter: 'invoke validate' to launch validation testing")
    print("📕 Enter: 'invoke --list' to have the whole menu list")
    print("")
    print("For more extensive documentation, please read `Readme.md` and `DeveloperGuide.md`")
    print("")
    print("Bye! 👋")



@task(splash)
def run(ctx, rebuild=False, cfg="dev", docker=False):
    """ 🚚 Build the web app (and then runs it if arg `--rebuild`). Runs in docker if `--docker` is specified. Optional args: [--rebuild] [--docker] [--cfg='dev|prod'] """
    print("\n🚚   Running Coding Challenge web app...")
    try:
        if rebuild:
            cmd = ('inv build')
            result = ctx.run(cmd, hide=False, warn=True)

        cmd = ('./run_server.sh ' + cfg)
        if docker:
            cmd = ('./run_server_in_docker.sh')

        result = ctx.run(cmd, hide=False, warn=True)
        if not result.ok:
            raise Exception("Error during running the server!")

    except Exception as excp:
        print("...with an error! 😡")
        print(excp)
        sys.exit(-1)

    print("\n👋  Closing Coding Challenge app! Bye!")
