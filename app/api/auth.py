from flask import Blueprint, request
from app.services.auth import (
    jwt_refresh_token_required,
    get_jwt_identity,
    get_tokens,
    get_access_token
)
from app.services.utils import build_response
from app.services import user as user_service

blueprint = Blueprint('auth', __name__)


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

    user = user_service.get_user_by_login(login)
    if login != user.login:  # or password_hash != sample_user.password_hash:
        return build_response(message="Bad login or password"), 401

    tokens = get_tokens(sample_user)
    return build_response(
        access_token=tokens["access_token"],
        refresh_token=tokens["refresh_token"]), 200


@blueprint.route('/refresh-token', methods=['POST'])
@jwt_refresh_token_required
def refresh_token():
    login = get_jwt_identity()

    # user = user_service.get_user_by_login(login)
    access_token = get_access_token(login)
    return build_response(access_token=access_token), 200
