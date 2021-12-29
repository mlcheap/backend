from model.project import find_project_by_id
from model.customer import find_customer_by_token
from model.task import find_tasks


def get_tasks_process(token, project_id, completed_before, completed_after, created_after, created_before, status, ):
    project = find_project_by_id(project_id)
    customer = find_customer_by_token(token)
    tasks = []
    if project and project["customer_id"] == str(customer["_id"]):
        tasks = find_tasks(str(project["_id"]), completed_before, completed_after, created_after, created_before,
                           status)
    return tasks
