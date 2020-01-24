from flask import jsonify


def build_response(access_token=None, refresh_token=None, message=None):
    resp = {}
    if access_token:
        resp['access_token'] = access_token
    if refresh_token:
        resp['refresh_token'] = refresh_token
    if message:
        resp['message'] = message

    return jsonify(resp)
