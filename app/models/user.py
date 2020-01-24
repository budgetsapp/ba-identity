# This is an example of a complex object that we could build
# a JWT from. In practice, this will likely be something
# like a SQLAlchemy instance.

from app.extensions import db


class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    display_name = db.Column(db.String(50))
    password_hash = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.display_name
