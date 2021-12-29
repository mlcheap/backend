from flask_jwt_extended import (
    create_access_token)

from Exceptions.AuthExceptions import UserAlreadyExistsException
from .utils import get_expire
from model.labeler import create_labeler, find_labeler_by_email


def signup_process(email, password, name, gender):
    user = find_labeler_by_email(email)
    if user:
        raise UserAlreadyExistsException

    create_labeler(email, name, password, gender)
    expires = get_expire()
    user = find_labeler_by_email(email)
    access_token = create_access_token(identity=str(user["_id"]), expires_delta=expires)

    return user, access_token
