from flask import request
from flask_restful import Resource
from resources.helpers import generate_api_response
from ..Resources.GetTasksResource import GetTasksResource
from ..Resources.GetTasksCountResource import GetTasksCountResource
from ..Resources.CreateTaskResource import CreateTaskResource
from ..controller.task.create_task_controller import create_task_process
from ..controller.task.get_task_controller import get_task_process
from ..controller.task.cancel_task_controller import cancel_task_process
from ..controller.task.get_tasks_controller import get_tasks_process
from ..controller.task.get_tasks_count_controller import get_tasks_count_process
from consts import BAD_REQUEST_CODE, NOT_EXISt_MESSAGE


class CreateTask(Resource):
    def post(self):
        unique_id = None
        callback = None
        req = request.get_json()
        items = req['items']
        task_type = req["task-type"]
        if "unique-id" in req:
            unique_id = req["unique-id"]
        if "callback" in req:
            callback = req["callback"]
        project_id = request.headers["project_id"]
        token = request.headers["token"]

        status, message, task = create_task_process(token,
                                                    project_id,
                                                    callback,
                                                    task_type,
                                                    items,
                                                    unique_id)
        if not status:
            return generate_api_response(message=message, status=BAD_REQUEST_CODE)

        return generate_api_response(data=task, response_class=CreateTaskResource)


class GetTask(Resource):
    def get(self):
        token = request.headers["token"]
        project_id = request.headers["project_id"]
        task_id = request.args.get("task_id")
        task = get_task_process(token, project_id, task_id)
        if task:
            return generate_api_response(data=task, response_class=CreateTaskResource)
        else:
            return generate_api_response(message=NOT_EXISt_MESSAGE.format("task"), status=BAD_REQUEST_CODE)


class GetTasks(Resource):
    def get(self):
        token = request.headers["token"]
        project_id = request.headers["project_id"]
        created_after = request.args.get("created_after")
        created_before = request.args.get("created_before")
        completed_before = request.args.get("completed_before")
        completed_after = request.args.get("completed_after")
        status = request.args.get("status")

        tasks = get_tasks_process(token, project_id, completed_before, completed_after, created_after, created_before,
                                  status)
        if not tasks:
            tasks = []
        return generate_api_response(data={"tasks": tasks, "project_id": project_id},
                                     response_class=GetTasksResource)


class GetTasksCount(Resource):
    def get(self):
        token = request.headers["token"]
        project_id = request.headers["project_id"]
        created_after = request.args.get("created_after")
        created_before = request.args.get("created_before")
        completed_before = request.args.get("completed_before")
        completed_after = request.args.get("completed_after")
        status = request.args.get("status")

        count = get_tasks_count_process(token, project_id, completed_before, completed_after, created_after,
                                        created_before,
                                        status)
        return generate_api_response(data=count, response_class=GetTasksCountResource)


class CancelTask(Resource):
    def delete(self):
        token = request.headers["token"]
        project_id = request.headers["project_id"]
        task_id = request.args.get("task_id")
        task = cancel_task_process(token, project_id, task_id)
        if task == -1:
            return generate_api_response(message=NOT_EXISt_MESSAGE.format("task"), status=BAD_REQUEST_CODE)

        return generate_api_response(data=task, response_class=CreateTaskResource)
