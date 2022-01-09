from pymongo import MongoClient
from _env import MONGO_URI, REDIS_HOST, REDIS_PORT
import redis
from applications.labeler.app import create_app as create_labeler_app
from applications.server_api.app import create_app as create_api_app
from dispatcher import SubdomainDispatcher
from werkzeug.serving import run_simple
import os

MO_URL = os.getenv('MONGO_URL') or MONGO_URI

db = MongoClient(MO_URL)['labeler']
rdb = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


def create_app():
    server_api_app = create_api_app()
    labeler_app = create_labeler_app()
    application = SubdomainDispatcher({'api': server_api_app, 'labeler': labeler_app})
    return application


if __name__ == '__main__':
    app = create_app()
    run_simple('localhost', 6221, app, use_reloader=True, use_debugger=True, use_evalex=True)
