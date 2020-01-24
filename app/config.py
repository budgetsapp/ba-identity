import os


class Config:
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

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
