from resources.errors import ApiException
from resources.messages import Message
from resources.helpers import generate_api_response, Status


class WrongCredentialException(ApiException):
    message = Message.WRONG_LOGIN_MESSAGE


class UserAlreadyExistsException(ApiException):
    message = Message.EMAIL_EXIST_MESSAGE


class UserNotExistsException(ApiException):
    message = Message.USER_NOT_EXIST_MASSAGE


class UnauthorizedException(ApiException):
    message = Message.EXPIRATION_TOKEN_MESSAGE
    status = Status.HTTP_UNAUTHORIZED


class ProjectNotExistException(ApiException):
    message = Message.EXPIRATION_TOKEN_MESSAGE
