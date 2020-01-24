import os


class Config:
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

    JWT_ACCESS_TOKEN_EXPIRES = 900  # s, = 15 min
    JWT_REFRESH_TOKEN_EXPIRES = 604800  # s, = 7 days
    JWT_ERROR_MESSAGE_KEY = 'message'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    @property
    def JWT_SECRET_KEY(self):
        return os.getenv("JWT_SECRET_KEY", None)


class ProdConfig(Config):
    FLASK_ENV = 'production'


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class TestConfig(Config):
    FLASK_ENV = 'testing'
    TESTING = True
