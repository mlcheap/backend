from functools import wraps

from flask import jsonify, request
from flask_sieve import Validator

from consts import BAD_REQUEST_CODE, OK_CODE, REQUEST_MUST_BE_JSON_MESSAGE, SUCCESS_MESSAGE, \
    FAILED_MESSAGE, MISSING_MESSAGE
from resources.errors import ValidJsonException, ApiException


def json_error_response():
    return send({}, message=REQUEST_MUST_BE_JSON_MESSAGE, code=BAD_REQUEST_CODE)


def send(data, message=SUCCESS_MESSAGE, meta={}, code=OK_CODE):
    if not code == OK_CODE and message == SUCCESS_MESSAGE:
        message = FAILED_MESSAGE
    return jsonify(data=data, message=message, meta=meta), code


def validate_json(Request):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            req = Request()
            print(req)
            if not request.is_json:
                raise ValidJsonException

            validator = Validator(rules=req.rules(), request=request)
            if validator.fails():
                messages = []
                for message in validator.messages().values():
                    messages.extend(message)
                raise ApiException(message='\n'.join(messages), meta={'errors': validator.messages()})
            return fn(*args, **kwargs)

        return wrapper

    return decorator


def validate_request_missing(*args):
    req = args[0]
    for arg in args[1:]:
        if arg not in req:
            return False, send({}, message=MISSING_MESSAGE.format(arg), code=BAD_REQUEST_CODE)
    return True, ""


def string_to_list_conversion(string):
    if len(string) <= 2:
        return []
    return string[1:-1].split(',')
