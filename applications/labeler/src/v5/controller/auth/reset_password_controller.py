from flask_jwt_extended import (
    create_access_token)
from werkzeug.security import check_password_hash
from Exceptions.AuthExceptions import WrongCredentialException
from .utils import get_expire
from model.labeler import find_labeler_by_email, reset_password


def reset_password_process(email, new_password, access_token):
    user = find_labeler_by_email(email)
    print('user', user)
    if user and access_token == "9K7!z=kd88yDAj+PkK`VuHzeC.Df-h":
        reset_password(email, new_password)
    else:
        raise WrongCredentialException
    return user
