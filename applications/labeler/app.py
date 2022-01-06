import os
from flask import Flask, Blueprint, request
from flask_jwt_extended import JWTManager
from flask_restful import Api
from _env import VERSION

blacklist = set()
version_prefix = f'/{VERSION}'
cwd = os.getcwd()


def create_app():
    import logging
    logging.basicConfig(filename='error.log', level=logging.ERROR)

    app = Flask(__name__)
    app.config.from_pyfile('_env.py')
    app.config['PROPAGATE_EXCEPTIONS'] = True
    jwt = JWTManager(app)

    with app.app_context():
        blue_print = Blueprint('api', __name__)
        api = Api(blue_print)

        from .src.v5.view.routes import initialize_routes
        initialize_routes(api)
        app.register_blueprint(blue_print, url_prefix=version_prefix)

        @jwt.expired_token_loader
        def my_expired_token_callback(jwt_header, jwt_payload):
            from src.resources.errors import UnauthorizedException
            return UnauthorizedException().response()

    return app


if __name__ == "__main__":
    app = create_app()


    @app.errorhandler(404)
    def page_not_found(e):
        print(request.path)
        return request.path


    @app.after_request
    def after_request(response):
        # response.headers.add('Access-Control-Allow-Origin', '*')
        # response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        # response.headers.add('Access-Control-Allow-Headers', '*')
        # response.headers.add('Access-Control-Allow-Methods', "*")
        # response.headers.add("Access-Control-Allow-Origin", "*")
        # response.headers.add("Access-Control-Allow-Headers", "*")
        # response.headers.add("Access-Control-Allow-Methods", "*")

        return response


    app.run(host='0.0.0.0', port=5100, debug=True, threaded=True)
