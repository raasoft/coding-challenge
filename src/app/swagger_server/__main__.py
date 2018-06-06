#!/usr/bin/env python3

import sys
import os
import connexion

from swagger_server import encoder
from flask_cors import CORS

from swagger_server.config import Config, DevelopmentConfig, TestConfig, ProductionConfig

appCfg = Config

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Configuration Manager'})
    
    app.run(port=appCfg.PORT, host=appCfg.HOST)

if __name__ == '__main__':
    env = sys.argv[1] if len(sys.argv) > 2 else 'dev'
    
    if env == 'dev':
        appCfg = DevelopmentConfig
    elif env == 'test':
        appCfg = TestConfig
    elif env == 'prod':
        appCfg = ProductionConfig
    else:
        raise ValueError('Invalid environment name')

    if "DOCKER_HOST" in os.environ:
        appCfg.HOST = os.getenv('DOCKER_HOST', appCfg.HOST)
        print("🐳  DOCKERIZED ENVIRONMENT")

    main()
