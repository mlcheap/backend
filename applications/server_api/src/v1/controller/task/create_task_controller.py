from model.task import create_task
from model.customer import find_customer_by_token
from model.project import find_project_by_id
from model.task_parsers import task_parser


# from model.cache import cache_tasks


def create_task_process(token, project_id, callback, task_type, items, unique_id):
    project = find_project_by_id(project_id)
    customer = find_customer_by_token(token)
    if not project or project["customer_id"] != str(customer["_id"]):
        message = "there is no project"
        print(message)
        return False, message, []

    task_obj = task_parser(task_type, items)
    # status, message = task_obj.pars_json()
    # if not status:
    #     return status, message, []
    customer_id = str(customer["_id"])
    task = create_task(customer_id,
                       str(project["_id"]),
                       [callback],
                       task_obj.to_dict(),
                       unique_id)
    task["project_id"] = project_id
    # cache_tasks(customer_id, project_name, [str(task["_id"])])
    return True, "", task
