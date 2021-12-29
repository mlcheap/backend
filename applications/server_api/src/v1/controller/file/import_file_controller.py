from model.file import save_requests_content, insert_file_info, get_file_path, get_file_dir
from model.customer import find_customer_by_token
import requests


def import_file_process(token, file_url, file_name):
    response = requests.get(file_url)

    customer = find_customer_by_token(token)
    file_dir = get_file_dir(str(customer["_id"]))
    size = len(response.content)

    created_at, updated_at, mime_type, file_id, file_name = \
        insert_file_info(str(customer["_id"]), file_dir, file_name, size)
    file_saved_name = str(file_id) + "." + file_name.rsplit('.', 1)[1].lower()
    file_path = get_file_path(file_dir, file_saved_name)
    save_requests_content(response, file_path)

    return {"created_at": created_at,
            "updated_at": updated_at,
            "mime_type": mime_type,
            "file_id": file_id,
            "file_name": file_name}
