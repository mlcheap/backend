from flask import jsonify

from .messages import Message


class Status:
    HTTP_OK = 200
    HTTP_BAD_REQUEST = 400
    HTTP_UNAUTHORIZED = 401
    HTTP_NOT_FOUND = 404
    HTTP_UNPROCESSABLE_ENTITY = 422


def generate_api_response(data={}, message=Message.SUCCESS_MESSAGE, status=Status.HTTP_OK, response_class=None,
                          meta={}):
    if response_class is not None:
        res = response_class(data)
        data = res.to_dict()
    response = jsonify(data=data, message=message, meta=meta)
    response.status_code = status
    return response

