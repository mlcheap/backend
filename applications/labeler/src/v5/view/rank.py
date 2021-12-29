from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from resources.helpers import generate_api_response
from ..controller.ranking import ranking_db_process, ranking_info_process


class RankDB(Resource):
    @jwt_required()
    def get(self):
        lang = request.args.get('lang')
        dbname = request.args.get('dbname')
        user_id = get_jwt_identity()
        rank, ranking, message, code = ranking_db_process(user_id, dbname, lang)
        return generate_api_response({'ranking': ranking, 'labeler-rank': rank})


class RankInfo(Resource):
    @jwt_required()
    def get(self):
        lang = request.args.get('lang')
        user_id = get_jwt_identity()
        dbs_ranking, total_ranking, message, code = ranking_info_process(user_id, lang)
        return generate_api_response({'dbs_rank': dbs_ranking, 'total_rank': total_ranking})
