from flask import jsonify

from ecommerce_api.factory import jwt
from users.models import User


def add_claims_to_access_token(identity):
    return {
        "user_id": identity.id,
        "username": identity.username,
        "roles": [role.name for role in identity.roles],
    }


def no_jwt_for_protected_endpoint(error_message):
    return jsonify({"success": False, "full_messages": [error_message]})


def user_loader(user_id):
    return User.query.get(user_id)


def identity_loader(user):
    return user.id


def token_revoked():
    return jsonify({"success": False, "full_messages": ["Revoked token"]})


def invalid_token_loader(error_message):
    return jsonify({"success": False, "full_messages": [error_message]})


jwt.user_loader_callback_loader(user_loader)

jwt.user_identity_loader(identity_loader)
jwt.user_claims_loader(add_claims_to_access_token)


@jwt.expired_token_loader
def valid_but_expired_token(expired_token):
    token_type = expired_token["type"]
    return jsonify({"success": False, "full_messages": ["Token expired"]}), 401


def validate_file_upload(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in [
        "png",
        "jpeg",
        "jpg",
    ]
