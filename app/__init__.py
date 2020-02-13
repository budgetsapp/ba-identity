import os

from flask import Flask
from flask_cors import CORS

from .extensions import auth, db
from app.api.auth import blueprint as auth_blueprint
from app import cli


config = {
    "dev-docker": "app.config.DevDockerConfig",
    'dev': 'app.config.DevConfig',
    'prod': 'app.config.ProdConfig',
    'test': 'app.config.TestConfig'
}

app = Flask(__name__, instance_relative_config=True)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


def create_app():
    config_name = os.getenv('FLASK_CONFIG', 'dev')

    # app.config.from_object(config[config_name])
    from werkzeug.utils import import_string
    config_object = import_string(config[config_name])()
    app.config.from_object(config_object)
    print('===> Config name', config_name)
    print('===> SQLALCHEMY_DATABASE_URI',
          config_object.SQLALCHEMY_DATABASE_URI)

    auth.init_app(app)
    app.register_blueprint(auth_blueprint, url_prefix='/v1')

    db.init_app(app)
    cli.init_cli_commands(app)

    return app
