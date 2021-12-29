from model.classes import create_class
from model.customer import find_customer_by_token
from model.project import find_project_by_id


def create_classes_process(token,
                           project_id,
                           classes):
    project = find_project_by_id(project_id)
    customer = find_customer_by_token(token)
    if not project or project["customer_id"] != str(customer["_id"]):
        message = "there is no project"
        print(message)
        return False, message, []

    customer_id = str(customer["_id"])
    results = []
    for _class in classes:
        res = create_class(customer_id,
                           project_id,
                           _class["name"],
                           _class["metadata"],
                           _class["unique-id"])
        results.append(res)
    # cache_tasks(customer_id, project_name, [str(task["_id"])])
    return True, "", results
