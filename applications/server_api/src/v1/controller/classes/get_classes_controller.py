from model.project import find_project_by_id
from model.customer import find_customer_by_token
from model.classes import find_classes


def get_classes_process(token, project_id):
    project = find_project_by_id(project_id)
    customer = find_customer_by_token(token)
    if project and project["customer_id"] == str(customer["_id"]):
        classes = list(find_classes(project_id))
        return classes
    return []
