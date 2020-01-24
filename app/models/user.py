# This is an example of a complex object that we could build
# a JWT from. In practice, this will likely be something
# like a SQLAlchemy instance.


class User:
    def __init__(self, login, display_name, roles):
        self.login = login
        self.roles = roles
        self.display_name = display_name

    @property
    def password_hash(self):
        return 'hash'
