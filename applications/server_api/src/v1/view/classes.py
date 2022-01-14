from flask import request
from flask_restful import Resource
from resources.helpers import generate_api_response
from ..Resources.GetClassesResource import GetClassesResource
from ..Resources.CreateClassResource import CreateClassResource
from ..controller.classes import cancel_class_process, get_class_process, get_classes_process, \
    get_classes_count_process, create_class_process, create_classes_process
from consts import BAD_REQUEST_CODE, NOT_EXISt_MESSAGE


class CreateClass(Resource):
    def post(self):
        unique_id = None
        req = request.get_json()
        project_id = req["project_id"]
        if "unique-id" in req:
            unique_id = req["unique-id"]
        name = req["name"]
        metadata = req["metadata"]
        token = request.headers["token"]

        status, message, _class = create_class_process(token,
                                                       project_id,
                                                       name,
                                                       metadata,
                                                       unique_id)
        if not status:
            return generate_api_response(message=message, status=BAD_REQUEST_CODE)

        return generate_api_response(data=_class, response_class=CreateClassResource)


class CreateClasses(Resource):
    def post(self):
        req = request.get_json()
        classes = req["classes"]
        for _class in classes:
            if "unique-id" not in _class:
                _class["unique-id"] = None
        project_id = req["project_id"]
        token = request.headers["token"]

        status, message, classes = create_classes_process(token,
                                                          project_id,
                                                          classes)
        if not status:
            return generate_api_response(message=message, status=BAD_REQUEST_CODE)

        return generate_api_response(data={"classes": classes}, response_class=GetClassesResource)


class GetClass(Resource):
    def get(self):
        token = request.headers["token"]
        project_id = request.headers["project_id"]
        class_id = request.args.get("class_id")
        _class = get_class_process(token, project_id, class_id)
        if _class:
            return generate_api_response(data=_class, response_class=CreateClassResource)
        else:
            return generate_api_response(message=NOT_EXISt_MESSAGE.format("classes"), status=BAD_REQUEST_CODE)


class GetClasses(Resource):
    def get(self):
        token = request.headers["token"]
        project_id = request.headers["project_id"]
        classes = get_classes_process(token, project_id)
        if not classes:
            classes = []
        # print(classes)
        return generate_api_response(data={"classes": classes},
                                     response_class=GetClassesResource)

# class CancelClass(Resource):
#     def delete(self):
#         token = request.headers["token"]
#         project_id = request.headers["project_id"]
#         class_id = request.args.get("class_id")
#         _class = cancel_task_process(token, project_id, class_id)
#         if _class == -1:
#             return generate_api_response(message=NOT_EXISt_MESSAGE.format("_class"), status=BAD_REQUEST_CODE)
#
#         return generate_api_response(data=_class, response_class=CreateClassResource)
