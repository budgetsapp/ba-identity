import os

from flask import Flask
from app.api import auth

config = {
    'dev': 'app.config.DevConfig',
    'prod': 'app.config.ProdConfig',
    'test': 'app.config.TestConfig'
}

app = Flask(__name__, instance_relative_config=True)


def create_app():
    config_name = os.getenv('FLASK_CONFIG', 'dev')

    # app.config.from_object(config[config_name])
    from werkzeug.utils import import_string
    config_object = import_string(config[config_name])()
    app.config.from_object(config_object)

    app.register_blueprint(auth.blueprint)

    return app
