from flask import request
from flask_restful import Resource
from resources.helpers import generate_api_response
from ..Resources.CreateProjectResource import CreateProjectResource
from ..Resources.GetAllProjectsResource import GetAllProjectsResource
from ..Resources.GetProjectResource import GetProjectResource
from ..controller.project.create_project_controller import create_project_process
from ..controller.project.get_all_projects_controller import get_all_projects_process
from ..controller.project.get_project_controller import get_project_process
from ..controller.project.update_project_controller import update_project_process
from resources.errors import ApiException
import traceback
from consts import OK_CODE


class CreateProject(Resource):
    def post(self):
        req = request.get_json()
        token = request.headers["token"]
        project_name = req["project_name"]
        metadata = req["metadata"]
        model_id = req["model_id"]
        labels_per_task = 1
        icon_id = ""
        if "labels_per_task" in req:
            labels_per_task = req["labels_per_task"]
        if "icon-id" in req:
            icon_id = req["icon-id"]
        try:
            status, message, project_id = create_project_process(project_name, token, labels_per_task, icon_id,
                                                                 metadata, model_id)
            if status == OK_CODE:
                return generate_api_response(data={
                    "project_name": project_name,
                    "project_id": project_id,
                    "labels_per_task": labels_per_task,
                    "metadata": metadata,
                    "model_id": model_id,
                    "icon_id": icon_id},
                    response_class=CreateProjectResource)
            else:
                return generate_api_response({}, message=message, status=status)
        except ApiException as e:

            return e.response()


class GetAllProjects(Resource):
    def get(self):
        token = request.headers["token"]
        try:
            print('get all p roject', token)
            projects = get_all_projects_process(token)
            return generate_api_response(data={"projects": projects},
                                         response_class=GetAllProjectsResource)
        except Exception as e:
            print(traceback.format_exc())

            return "error"


class GetProject(Resource):
    def get(self):
        token = request.headers["token"]
        project_id = request.headers["project_id"]
        try:
            project, project_stat = get_project_process(token, project_id)
            project["stat"] = project_stat
            return generate_api_response(data=project,
                                         response_class=GetProjectResource)
        except Exception as e:
            print(traceback.format_exc())

            return "error"


class EditProject(Resource):
    def put(self):
        token = request.headers["token"]
        project_id = request.headers["project_id"]
        req = request.get_json()
        new_project_conf = req
        try:
            edited_project = update_project_process(token,
                                                    project_id,
                                                    new_project_conf)
            edited_project["project_id"] = str(edited_project["_id"])
            return generate_api_response(data=edited_project, response_class=CreateProjectResource)
        except Exception as e:
            print(traceback.format_exc())
        return "error"
