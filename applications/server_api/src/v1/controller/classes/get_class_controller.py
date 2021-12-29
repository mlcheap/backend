from model.project import find_project_by_id
from model.customer import find_customer_by_token
from model.classes import find_class
from model.label import find_task_labels


def get_class_process(token, project_id, class_id):
    project = find_project_by_id(project_id)
    customer = find_customer_by_token(token)
    if project and project["customer_id"] == str(customer["_id"]):
        _class = find_class(project_id, class_id)
        return _class
