from flask import request, send_file
from flask_restful import Resource
from resources.helpers import generate_api_response
from ..Resources.UploadFileResource import UploadFileResource
from ..controller.file.upload_file_controller import upload_file_process
from ..controller.file.import_file_controller import import_file_process
from ..controller.file.download_file_controller import download_file_process
import traceback


class UploadFile(Resource):
    def post(self):
        try:
            # print(dict(request.form).keys())
            token = request.headers["token"]
            file = request.files['document']
            data = upload_file_process(token, file)
            return generate_api_response(data=data,
                                         response_class=UploadFileResource)

        except Exception as e:
            print(traceback.format_exc())
            return traceback.format_exc()


class ImportFile(Resource):
    def post(self):
        token = request.headers["token"]
        req = request.get_json()
        file_url = req['file_url']
        try:
            data = import_file_process(token, file_url, file_url.rsplit('/', 1)[1])
            return generate_api_response(data=data,
                                         response_class=UploadFileResource)
        except Exception as e:
            print(traceback.format_exc())
            return "error "


class DownloadFile(Resource):
    def get(self):
        token = request.headers["token"]
        # print("token", token)
        file_id = request.args.get("file-id")
        file_path, mimetype = download_file_process(token, file_id)
        return send_file(file_path, mimetype='image/gif')
