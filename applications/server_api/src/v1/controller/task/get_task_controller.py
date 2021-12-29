from model.project import find_project_by_id
from model.customer import find_customer_by_token
from model.task import find_task
from model.label import find_task_labels


def get_task_process(token, project_id, task_id):
    project = find_project_by_id(project_id)
    customer = find_customer_by_token(token)
    if project and project["customer_id"] == str(customer["_id"]):
        task = find_task(str(project["_id"]), task_id)
        labels = find_task_labels(project_id, task_id)
        if task:
            task["project_id"] = project_id
            task["labels"] = labels
        return task
