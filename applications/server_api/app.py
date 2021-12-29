from pymongo import MongoClient
from _env import MONGO_URI, REDIS_HOST, REDIS_PORT
from flask import Flask, Blueprint, request
import redis
from flask_restful import Api

VERSION1 = "v1"
version_prefix1 = f'/{VERSION1}'
db = MongoClient(MONGO_URI)['labeler']
rdb = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


def create_app():
    import logging
    logging.basicConfig(filename='error.log', level=logging.ERROR)

    app = Flask(__name__)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.config.from_pyfile('_env.py')
    with app.app_context():
        api_bp = Blueprint('api', __name__)
        api_v1 = Api(api_bp)
        from .src.v1.view.routers import initialize_routes
        initialize_routes(api_v1)
        app.register_blueprint(api_bp, url_prefix=version_prefix1)

    @app.errorhandler(404)
    def page_not_found(e):
        print(request.path)
        return request.path

    return app


if __name__ == '__main__':
    app = create_app()
    app.run('0.0.0.0', port=6221, debug=True)
