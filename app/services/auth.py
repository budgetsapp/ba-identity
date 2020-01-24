from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_refresh_token_required as flask_jwt_extended_jwt_refresh_token_required
)


jwt_refresh_token_required = flask_jwt_extended_jwt_refresh_token_required
get_jwt_identity = get_jwt_identity


def _add_claims_to_access_token(user):
    return {
        'roles': user.roles,
        'display_name': user.display_name
    }


def _user_identity_lookup(user):
    return user.login


def get_tokens(user):
    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=user)
    refresh_token = create_refresh_token(identity=user)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


def get_access_token(user):
    access_token = create_access_token(identity=user)
    return access_token


class Auth:
    def __init__(self):
        self.jwt_manager = JWTManager()

        # Create a function that will be called whenever create_access_token
        # is used. It will take whatever object is passed into the
        # create_access_token method, and lets us define what custom claims
        # should be added to the access token.
        self.jwt_manager.user_claims_loader(_add_claims_to_access_token)

        # Create a function that will be called whenever create_access_token
        # is used. It will take whatever object is passed into the
        # create_access_token method, and lets us define what the identity
        # of the access token should be.
        self.jwt_manager.user_identity_loader(_user_identity_lookup)

    def init_app(self, app):
        self.jwt_manager.init_app(app)
