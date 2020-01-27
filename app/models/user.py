from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app.extensions import db


user_roles = db.Table('user_roles',
                      db.Column('role_id', db.String(36), db.ForeignKey(
                          'role.id'), primary_key=True),
                      db.Column('user_id', db.String(36), db.ForeignKey(
                          'user.id'), primary_key=True)
                      )


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

    def get_role_names(self):
        return [role.display_name for role in self.roles]

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User display_name={self.display_name} roles={self.roles}"


class Role(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    display_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Role display_name={self.display_name}>"
