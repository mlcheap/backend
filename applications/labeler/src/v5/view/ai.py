from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from resources.helpers import generate_api_response
from consts import OK_CODE
from ..controller.label import new_task_process, set_labels_tasks_process, get_project_process, ai_predict_process
from ..view.utils import string_to_list_conversion


class Ai(Resource):
    @jwt_required()
    def post(self):
        lang = request.args.get('lang')
        req = request.get_json()

        project_id, task_id, excludes = \
            req['project_id'], req['task_id'], req["excludes"]

        user_id = get_jwt_identity()

        labels = ai_predict_process(user_id,
                                    project_id,
                                    task_id,
                                    excludes)
        return generate_api_response({'labels': labels})
