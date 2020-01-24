from app.models.user import User


def get_user_by_login(login):
    return User.query.filter_by(login=login).first()
