from model.file import find_file_path
from model.customer import find_customer_by_token
from app import db

file_db = db["file_db"]


def download_file_process(token, file_id):
    customer = find_customer_by_token(token)
    return find_file_path(str(customer["_id"]), file_id)
