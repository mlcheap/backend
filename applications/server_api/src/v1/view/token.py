from flask import request
from flask_restful import Resource
from resources.helpers import generate_api_response
from ..controller.token import create_customer_process, create_token_process
from ..Resources.CreateTokenResource import CreateTokenResource
from consts import OK_CODE
import traceback


class GetToken(Resource):
    def post(self):
        req = request.get_json()
        username = req["username"]
        password = req["password"]
        if username == "root" and password == "xHe>MARq7yBt-=4*":
            try:
                customer_id = create_customer_process(username, password)
                token = create_token_process(customer_id)
                return generate_api_response(data={"token": token},
                                             response_class=CreateTokenResource)
            except Exception as e:
                print(traceback.format_exc())
                return "error"
        return generate_api_response(data={}, message="customer not exist", status=OK_CODE)
