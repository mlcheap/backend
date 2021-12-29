from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from resources.helpers import generate_api_response
from consts import OK_CODE
from ..controller.label import new_task_process, set_labels_tasks_process, get_project_process, ai_predict_process
from ..view.utils import string_to_list_conversion


class GetProject(Resource):
    @jwt_required()
    def get(self):
        project_id = request.args.get('project_id')
        lang = request.args.get('lang')
        user_id = get_jwt_identity()
        status, message, project = get_project_process(user_id,
                                                       project_id,
                                                       lang)
        if not status == OK_CODE:
            return generate_api_response({}, message=message, status=status)
        return generate_api_response({'project': {"project_name": project['project_name'],
                                                  "metadata": project["metadata"]}})


class NewTask(Resource):
    @jwt_required()
    def get(self):
        project_id = request.args.get('project_id')

        buffer_ids = string_to_list_conversion(request.args.get('buffer_ids', default='[]'))
        skiped_ids = string_to_list_conversion(request.args.get('skiped_ids', default='[]'))
        lang = request.args.get('lang')
        user_id = get_jwt_identity()
        items, stat, message, code = new_task_process(project_id,
                                                      user_id,
                                                      buffer_ids,
                                                      skiped_ids,
                                                      lang)
        if not code == OK_CODE:
            return generate_api_response({}, message=message, status=code)
        exists = (len(items) > 0)
        return generate_api_response({'tasks': items}, meta={'exists': exists, **stat, "project_id": project_id})


class LabelTask(Resource):
    @jwt_required()
    def post(self):
        lang = request.args.get('lang')
        req = request.get_json()

        project_id, task, buffer_ids, skiped_ids = \
            req['project_id'], req['task'], req["buffer_ids"], req["skiped_ids"]

        user_id = get_jwt_identity()

        items, stat, message, code = set_labels_tasks_process(user_id,
                                                              project_id,
                                                              task,
                                                              buffer_ids,
                                                              skiped_ids,
                                                              lang)
        if not code == OK_CODE:
            return generate_api_response({}, message=message, status=code)
        exists = (len(items) > 0)
        return generate_api_response({'tasks': items}, meta={'exists': exists, **stat, 'project_id': project_id})


