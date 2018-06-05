from invoke import task
import shutil
import os

sourceBasePath = "src/app/"
buildBasePath = "build/app/"
zipFilename = "configuration_manager"

sourceFiles = ["requirements.txt", 
               "test-requirements.txt",

               "swagger_server/__main__.py",
               "swagger_server/controllers/configuration_controller.py",

               "swagger_server/test/__init__.py",
               "swagger_server/test/test_configuration_controller.py",

               "swagger_server/controllers/fake_database.py"

              ]

deployFiles = ["build/app", 
               "build/docs",

               "run_server.sh",

               "Readme.md",
               "DeveloperGuide.md"
              ]

@task
def splash(ctx):
    """ Splash screen """
    print("\n\n✨✨✨ Coding Challenge web app")

@task
def clean(ctx):
    """ Clean target for the project """

    print("\n🗑  Cleaning the build directory...")
    try:
        result = shutil.rmtree("build", ignore_errors=True)
    except Exception as e:
        print("...with an error! 😡")
        print(e)
    
    print("...successfully! ✅")

@task(clean)
def generate(ctx):
    """ Generate source code target for the project """
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

        print("Updating generated files with updated business logic...")
        for f in sourceFiles:
            try:
                os.remove(buildBasePath+f)
            except OSError as e:
                if e.errno != 2:
                    raise e

            shutil.copy(sourceBasePath+f,buildBasePath+f)

    except Exception as e:
        print("...with an error! 😡")
        print(e)

    print("...successfully! ✅")

@task(generate)
def unittest(ctx):
    """ Unit test target for the project """
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
           raise Exception("Cannot run `tox` for unit testing")

        os.chdir("../..")

    except Exception as e:
        print("...with an error! 😡")
        print(e)

    
    print("\n...successfully! ✅")

@task(splash, generate, unittest)
def build(ctx):
    """ Build the whole project """
    print("\n🎉🎉🎉 Coding Challenge app built with success!\n")
    print("Run `./run_server.sh` to launch the web app")


@task(build)
def deploy(ctx):
    """ Deploys and creates an archive containing the whole app """

    print("\n📦 Creating zip file package in `deploy` folder...")

    try:
        result = shutil.rmtree("deploy", ignore_errors=True)

        os.makedirs("deploy")

        filesToZip = ' '.join(deployFiles)

        cmd = ('zip -q -r deploy/'+ zipFilename +'.zip '
               ""+filesToZip)
        result = ctx.run(cmd, hide=False, warn=True)
        if not result.ok:
            raise Exception("Cannot create zip file")

    except Exception as e:
        print("...with an error! 😡")
        print(e)
    
    print("...successfully! ✅")
    print("\n🎉🎉🎉 Coding Challenge app " + zipFilename + " created with success!\n")