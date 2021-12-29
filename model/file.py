import os
from app import db
import datetime
from bson import ObjectId

Data_Dir = os.path.join(os.getcwd(), 'datasets')
file_db = db["file_db"]


def get_file_dir(customer_id):
    c_dir = os.path.join(Data_Dir, customer_id)
    if not os.path.exists(c_dir):
        os.makedirs(c_dir)
    db_dir = os.path.join(c_dir, "files")
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    return db_dir


def get_file_path(db_dir, filename):
    return os.path.join(db_dir, filename)


def save_file(file, filepath):
    file.save(filepath)


def save_requests_content(res, filepath):
    with open(filepath, 'wb') as f:
        f.write(res.content)


def insert_file_info(customer_id, file_dir, filename, size):
    created_at = updated_at = datetime.datetime.utcnow()
    file_type = filename.rsplit('.', 1)[1].lower()
    mime_type = ""
    if file_type in ["png", "jpg", "jpeg"]:
        mime_type = "image/" + file_type
    file_id = file_db.insert_one({"created_at": created_at,
                                  "updated_at": updated_at,
                                  "customer_id": customer_id,
                                  "file_dir": file_dir,
                                  "file_name": filename,
                                  "size": size,
                                  "mime_type": mime_type}).inserted_id

    return created_at, updated_at, mime_type, str(file_id), filename


def exist_file(customer_id, file_id):
    if file_id != "":
        return file_db.count({"_id": ObjectId(file_id), "customer_id": customer_id}) > 0
    return False


def find_file_path(customer_id, file_id):
    file = file_db.find_one({"_id": ObjectId(file_id), "customer_id": customer_id})
    file_type = file['file_name'].rsplit('.', 1)[1].lower()
    file_saved_name = str(file["_id"]) + "." + file_type

    return os.path.join(file['file_dir'], file_saved_name), file['mime_type']
