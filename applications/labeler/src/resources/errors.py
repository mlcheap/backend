from src.resources.helpers import generate_api_response, Status
from src.resources.messages import Message


class ApiException(Exception):
    message = Message.FAILED_MESSAGE
    status = Status.HTTP_BAD_REQUEST
    meta = {}

    def __init__(self, message=None, status_code=None, data=None, meta=None):
        Exception.__init__(self)
        if message is not None:
            self.message = message
        if meta is not None:
            self.meta = meta
        if status_code is not None:
            self.status = status_code
        self.data = {} if data is None else data

    def response(self):
        return generate_api_response(data=self.data, message=self.message, status=self.status, meta=self.meta)


class UnauthorizedException(ApiException):
    message = Message.EXPIRATION_TOKEN_MESSAGE
    status = Status.HTTP_UNAUTHORIZED


class ValidJsonException(ApiException):
    message = Message.REQUEST_MUST_BE_JSON_MESSAGE


class MissingParamsException(ApiException):
    def __init__(self, param: list = []):
        self.message = Message.MISSING_MESSAGE.format(', '.join(param))
