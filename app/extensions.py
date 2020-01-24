from .services.auth import Auth
from flask_sqlalchemy import SQLAlchemy

auth = Auth()
db = SQLAlchemy()
