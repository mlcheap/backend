from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from _env import VERSION
from resources.helpers import generate_api_response
from ..Resources.InitResource import InitResource
from ..Resources.LabelerResource import LabelerResource
from ..controller.init import init_process


class Init(Resource):
    @jwt_required()
    def get(self):
        lang = request.args.get('lang')
        labeler_id = get_jwt_identity()
        labeler, projects, rank = init_process(lang, labeler_id)
        return generate_api_response(data={'projects': projects, 'rank': rank},
                                     response_class=InitResource,
                                     meta=LabelerResource(labeler).to_dict())
