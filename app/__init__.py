import os

from flask import Flask
from .extensions import auth
from app.api.auth import blueprint as auth_blueprint


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

    auth.init_app(app)
    app.register_blueprint(auth_blueprint)

    return app
