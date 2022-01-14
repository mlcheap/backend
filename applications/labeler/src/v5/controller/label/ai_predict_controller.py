from model.project import find_project_by_id
from model.task import find_task
from model.labeler import all_labelers_in_project, find_labeler_by_id
from resources.helpers import Status, Message
from applications.labeler.src.v5.ai.Client import Client


def req_ml_server(model_id, title, description, excludes):
    LABELER_TEST_API = 'e2fcd22b-4c71-4c37-a140-39835933edbe'

    client = Client(api_key=LABELER_TEST_API,)
    # print(model_id)
    response = client.predict({
        "id": model_id,
        "description": description,
        "title": title,
        "exclude_indices": []})
    # print(response)
    return response


def ai_predict_process(labeler_id,
                       project_id,
                       title, description,
                       excludes):
    project = find_project_by_id(project_id)
    labeler = find_labeler_by_id(labeler_id)
    customer_id = project["customer_id"]
    active_labelers, deactivated_labelers = all_labelers_in_project(customer_id, project_id)
    return req_ml_server(project["model_id"], title, description, excludes)
