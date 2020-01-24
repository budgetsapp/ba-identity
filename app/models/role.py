from app.extensions import db


class Role(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    display_name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Role %r>' % self.display_name
