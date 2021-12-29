from flask import request
from flask_jwt_extended import jwt_required, unset_jwt_cookies
from flask_restful import Resource
from flask import jsonify
from resources.helpers import generate_api_response
from ..Requests.AuthRequest import RegisterRequest, LoginRequest
from ..Resources.LabelerResource import LabelerResource
from ..controller.auth import login_process, signup_process
from ..view.utils import validate_json
from resources.errors import ApiException


class Signin(Resource):

    @validate_json(LoginRequest)
    def post(self):
        try:
            data = request.get_json()
            user, access_token = login_process(data['email'], data['password'])
        except ApiException as e:
            return e.response()

        return generate_api_response(data=user, response_class=LabelerResource, meta={'access_token': access_token})


class Signup(Resource):
    @validate_json(RegisterRequest)
    def post(self):
        data = request.get_json()
        try:
            new_user, access_token = signup_process(data['email'], data['password'],
                                                    data['name'], data['gender'])
        except ApiException as e:
            return e.response()

        return generate_api_response(data=new_user, response_class=LabelerResource, meta={'access_token': access_token})


class Logout(Resource):
    @jwt_required
    def delete(self):
        unset_jwt_cookies(jsonify({"message": "logout successful"}))
        return generate_api_response()
