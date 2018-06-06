# config.py
class Config:
    APP_NAME = 'myapp'
    HOST = 'localhost'
    PORT = '8080'
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class TestConfig(Config):
    DEBUG = True
    TESTING = True
 
class ProductionConfig(Config):
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = False