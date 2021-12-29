from flask_jwt_extended import (
    create_access_token)
from werkzeug.security import check_password_hash
from Exceptions.AuthExceptions import WrongCredentialException
from .utils import get_expire
from model.labeler import find_labeler_by_email


def login_process(email, password):
    user = find_labeler_by_email(email)
    if not user or not check_password_hash(user["password"], password):
        raise WrongCredentialException
    return user, create_access_token(identity=str(user["_id"]), expires_delta=get_expire())
