import os


class Config:
    DEBUG = False
    TESTING = False

    JWT_ACCESS_TOKEN_EXPIRES = 3600000  # s, = 60 min
    JWT_REFRESH_TOKEN_EXPIRES = 604800  # s, = 7 days
    JWT_ERROR_MESSAGE_KEY = 'message'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    @property
    def JWT_SECRET_KEY(self):
        return os.getenv("JWT_SECRET_KEY", None)


class ProdConfig(Config):
    pass


class LocalConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\Vadim\\Documents\\db\\db.sqlite'


class LocalMacConfig(LocalConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:////usr/local/db/db.sqlite'


class DevDockerConfig(Config):
    DEBUG = False
    FLASK_RUN_PORT = 8080
    SQLALCHEMY_DATABASE_URI = 'sqlite:////usr/db/db.sqlite'
