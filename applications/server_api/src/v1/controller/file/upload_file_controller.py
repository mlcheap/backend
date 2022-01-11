from model.file import save_file, insert_file_info, get_file_path, get_file_dir
from model.customer import find_customer_by_token
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file_process(token, file):
    customer = find_customer_by_token(token)

    if file and allowed_file(file.filename):
        blob = file.read()
        size = len(blob)
        file_name = secure_filename(file.filename)
        file_dir = get_file_dir(str(customer["_id"]))
        try:
            os.makedirs(file_dir)
        except OSError as exc:
            pass
        created_at, updated_at, mime_type, file_id, file_name = \
            insert_file_info(str(customer["_id"]), file_dir, file_name, size)
        file_saved_name = str(file_id) + "." + file_name.rsplit('.', 1)[1].lower()
        file_path = get_file_path(file_dir, file_saved_name)
        file.seek(0)
        save_file(file, file_path)

        return {"created_at": created_at,
                "updated_at": updated_at,
                "mime_type": mime_type,
                "file_id": file_id,
                "file_name": file_name}
