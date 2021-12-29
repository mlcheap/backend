from flask import request, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from resources.errors import MissingParamsException
from resources.helpers import generate_api_response
from ..controller.file import project_icon_process, image_process
from consts import OK_CODE


class Icon(Resource):
    def get(self):
        project_id = request.args.get('project_id')
        (icon_path, mimetype), message, code = project_icon_process(project_id)
        if not code == OK_CODE:
            return generate_api_response()
        return send_file(icon_path, mimetype=mimetype)


class Image(Resource):
    @jwt_required()
    def get(self):
        image_path, message, code = image_process(request.args["image_id"])
        if not code == OK_CODE:
            return generate_api_response()

        return send_file(image_path, mimetype='image/gif')
