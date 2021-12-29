from model.project import find_project_by_id
from model.customer import find_customer_by_token
from model.task import get_project_stat
from model.labeler import all_labelers_in_project
from model.label import get_project_total_labels


def get_project_process(customer_token, project_id):
    customer = find_customer_by_token(customer_token)
    project = find_project_by_id(project_id)
    if project["customer_id"] == str(customer["_id"]):
        project_stat = get_project_stat(project_id)
        active_labelers, deactivated_labelers = all_labelers_in_project(str(customer["_id"]), project_id)
        project_stat.update(
            {"labelers": {'active_labelers': active_labelers, 'deactivated_labelers': deactivated_labelers},
             "total_labels": get_project_total_labels(project_id)})
        return project, project_stat
