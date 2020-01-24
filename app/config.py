import os


class Config:
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class ProdConfig(Config):
    FLASK_ENV = 'production'


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class TestConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
