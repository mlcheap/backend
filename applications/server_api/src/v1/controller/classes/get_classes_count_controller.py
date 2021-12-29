from model.project import find_project_by_id
from model.customer import find_customer_by_token
from model.task import count_tasks


def get_classes_count_process(token, project_id, completed_before, completed_after, created_after, created_before, ):
    project = find_project_by_id(project_id)
    customer = find_customer_by_token(token)
    if project and project["customer_id"] == str(customer["_id"]):
        tasks = count_tasks(
            str(project["_id"]),
            completed_before,
            completed_after,
            created_after,
            created_before,
            status)
        return tasks
    return 0
