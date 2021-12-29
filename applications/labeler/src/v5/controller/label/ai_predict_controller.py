from model.project import find_project_by_id
from model.task import find_task
from model.labeler import all_labelers_in_project, find_labeler_by_id
from resources.helpers import Status, Message
from applications.labeler.src.v5.ai.Client import Client


def req_ml_server(model_id, task, excludes):
    LABELER_TEST_API = 'e2fcd22b-4c71-4c37-a140-39835933edbe'

    client = Client(LABELER_TEST_API)
    data = task["items"][0]["data"]
    response = client.predict({
        "id": model_id,
        "description": data['description'],
        "title": data["title"],
        "exclude_indices": excludes})
    return response


def ai_predict_process(labeler_id,
                       project_id,
                       task_id,
                       excludes):
    project = find_project_by_id(project_id)
    labeler = find_labeler_by_id(labeler_id)
    customer_id = project["customer_id"]
    active_labelers, deactivated_labelers = all_labelers_in_project(customer_id, project_id)
    if {"email": labeler['email'], "_id": labeler_id} in active_labelers:
        task = find_task(project_id, task_id)
        return req_ml_server(project["model_id"], task, excludes)
