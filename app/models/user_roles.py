from app.extensions import db

user_roles = db.Table('user_roles',
                      db.Column('role_id', db.String(36), db.ForeignKey(
                          'role.id'), primary_key=True),
                      db.Column('user_id', db.String(36), db.ForeignKey(
                          'user.id'), primary_key=True)
                      )
