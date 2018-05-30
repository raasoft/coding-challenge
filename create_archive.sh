#!/bin/sh
mkdir -p deploy
zip -r deploy/configuration_manager.zip build/app build/docs run_server.sh Readme.md DeveloperGuide.md
