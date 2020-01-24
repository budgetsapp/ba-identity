# This is an example of a complex object that we could build
# a JWT from. In practice, this will likely be something
# like a SQLAlchemy instance.
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.extensions import db
from .user_roles import user_roles


class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    display_name = db.Column(db.String(50))
    password_hash = db.Column(db.String(), nullable=False)
    roles = db.relationship('Role', secondary=user_roles,
                            lazy='subquery', backref=db.backref('users', lazy=True))

    @property
    def password(self):
        raise AttributeError('Password is not a readable')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.display_name
