from model.project import update_project, find_project_by_id
from model.customer import find_customer_by_token


# from model.cache import cache_create_project

def update_project_process(customer_token, project_id, new_project_conf):
    project = find_project_by_id(project_id)
    customer = find_customer_by_token(customer_token)

    if project and project["customer_id"] == str(customer["_id"]):
        for key in new_project_conf:
            if key not in ["labels_per_task", "icon_id", "project_name","model_id", "lang"]:
                return False
        return update_project(project, new_project_conf)

    # cache_create_project(project_name, customer_id, labels_per_task)
