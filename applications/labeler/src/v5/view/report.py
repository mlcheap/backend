from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from resources.helpers import generate_api_response
from ..controller.report import report_process


class Report(Resource):
    @jwt_required()
    def get(self):
        req = request.get_json()
        _from = req['from']
        to = req['to']
        user_id = get_jwt_identity()
        report, message, code = report_process(user_id, _from, to)
        return generate_api_response(data=report)
