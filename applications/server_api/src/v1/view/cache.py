from flask import request
from flask_restful import Resource
from resources.helpers import generate_api_response
from ..Resources.ResetCacheResource import ResetCacheResource

import traceback


class AddLabeler(Resource):
    def post(self):
        req = request.get_json()
        token = request.headers["token"]
        project_name = request.headers["project_name"]
        emails = req["emails"]
        try:
            reset_cache_process(project_name, token, emails)
            return generate_api_response(data={"token": token,
                                               "project_name": project_name},
                                         response_class=ResetCacheResource)
        except Exception as e:
            print(traceback.format_exc())
            return "error"