#!/usr/bin/env python3

import connexion

from swagger_server import encoder
from flask_cors import CORS

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    
    CORS(app.app)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Configuration Manager'})
    cfgPort = 8080
    cfgUrl = "127.0.0.1"
    #cfgUrl = "0.0.0.0"
    app.run(port=cfgPort, host=cfgUrl)

if __name__ == '__main__':
    main()
