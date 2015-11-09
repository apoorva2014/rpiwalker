import os

class Config(Object):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
