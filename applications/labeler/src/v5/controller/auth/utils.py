import datetime
from flask import current_app


def get_expire():
    return datetime.timedelta(days=current_app.config["TOKEN_EXPIRATION_DAYS"])
