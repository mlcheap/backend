from flask import request
from flask_restful import Resource
from resources.helpers import generate_api_response
from ..controller.labeler import add_labeler_process, cancel_labeler_process, all_labelers_process
from ..Resources.AddLabelerResource import AddLabelerResource

import traceback


class AddLabeler(Resource):
    def post(self):
        req = request.get_json()
        token = request.headers["token"]
        project_id = request.headers["project_id"]
        emails = req["emails"]
        try:
            active_labelers, deactivated_labelers = add_labeler_process(project_id, token, emails)
            return generate_api_response(data={"token": token,
                                               "project_id": project_id,
                                               "active_labelers": active_labelers,
                                               "deactivated_labelers": deactivated_labelers},
                                         response_class=AddLabelerResource)
        except Exception as e:
            print(traceback.format_exc())
            return "error"


class CancelLabeler(Resource):
    def delete(self):
        token = request.headers["token"]
        project_id = request.headers["project_id"]
        email = request.args.get("email")

        try:
            active_labelers, deactivated_labelers = cancel_labeler_process(project_id, token, email)
            return generate_api_response(data={"token": token,
                                               "project_id": project_id,
                                               "active_labelers": active_labelers,
                                               "deactivated_labelers": deactivated_labelers},
                                         response_class=AddLabelerResource)
        except Exception as e:
            print(traceback.format_exc())
            return "error"


class AllLabelers(Resource):
    def get(self):
        token = request.headers["token"]
        project_id = request.headers["project_id"]
        try:
            active_labelers, deactivated_labelers = all_labelers_process(project_id, token)
            return generate_api_response(data={"token": token,
                                               "project_id": project_id,
                                               "active_labelers": active_labelers,
                                               "deactivated_labelers": deactivated_labelers},
                                         response_class=AddLabelerResource)
        except Exception as e:
            print(traceback.format_exc())
            return "error"
