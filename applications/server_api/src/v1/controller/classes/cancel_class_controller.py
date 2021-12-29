from model.project import find_project_by_id
from model.customer import find_customer_by_token
from model.task import cancel_task, find_task
from model.cache.query import delete_cache_task


def cancel_class_process(token, project_id, class_id):
    project = find_project_by_id(project_id)
    customer = find_customer_by_token(token)
    if project and project["customer_id"] == str(customer["_id"]):
        task = find_task(project_id, task_id)
        if task:
            task = cancel_task(str(project["_id"]), task_id)
            # delete_cache_task(str(project["customer_id"]), project_name, task_id)
            task['project_id'] = project_id
            return task
        return -1
    return []
