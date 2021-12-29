from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from ..controller.classes.get_class_controller import get_class_process
from ..controller.classes.get_all_classes_controller import get_all_classes_process
from resources.helpers import generate_api_response
from ..Resources.CreateClassResource import CreateClassResource
from ..Resources.GetClassesResource import GetClassesResource


class GetClass(Resource):
    @jwt_required()
    def get(self):
        project_id = request.args.get('project_id')
        req = request.get_json()

        class_id = request.args.get('class_id')
        lang = request.args.get('lang')
        labeler_id = get_jwt_identity()
        _class = get_class_process(labeler_id,
                                   project_id,
                                   class_id)

        return generate_api_response(data=_class, response_class=CreateClassResource)


class GetAllClasses(Resource):
    @jwt_required()
    def get(self):
        project_id = request.args.get('project_id')
        req = request.get_json()

        lang = request.args.get('lang')
        labeler_id = get_jwt_identity()
        classes = get_all_classes_process(labeler_id,
                                          project_id)

        return generate_api_response(data={"classes": classes}, response_class=GetClassesResource)
