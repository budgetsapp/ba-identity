from flask import Blueprint, request
from app.services.auth import (
    jwt_refresh_token_required,
    get_jwt_identity,
    get_tokens,
    get_access_token
)
from app.services.utils import build_response
from app.models import user

blueprint = Blueprint('auth', __name__)

sample_user = user.User(
    login='test', display_name="User Name", roles=['foo', 'bar'])


@blueprint.route('/get-tokens', methods=['POST'])
def get_token():
    if not request.is_json:
        return build_response(message="Missing JSON in request"), 400
    login = request.json.get("login", None)
    password = request.json.get("password", None)

    if not login:
        return build_response(message="Missing 'login' parameter"), 400
    if not password:
        return build_response(message="Missing 'password' parameter"), 400

    password_hash = sample_user.password_hash  # check password hash
    # call db methods to check user
    if login != sample_user.login or password_hash != sample_user.password_hash:
        return build_response(message="Bad login or password"), 401

    tokens = get_tokens(sample_user)
    return build_response(
        access_token=tokens["access_token"],
        refresh_token=tokens["refresh_token"]), 200


@blueprint.route('/refresh-token', methods=['POST'])
@jwt_refresh_token_required
def refresh_token():
    current_user = get_jwt_identity()

    # get user from DB by identity
    print('=====> current user' + current_user)
    access_token = get_access_token(sample_user)
    return build_response(access_token=access_token), 200
