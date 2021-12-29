from model.project import find_project_by_id
from model.task import get_project_stat
from model.labeler import all_labelers_in_project, find_labeler_by_id
from resources.helpers import Status, Message


def get_project_process(labeler_id, project_id, lang):
    project = find_project_by_id(project_id)
    labeler = find_labeler_by_id(labeler_id)
    customer_id = project["customer_id"]
    active_labelers, deactivated_labelers = all_labelers_in_project(customer_id, project_id)
    if {"email":labeler['email'],"_id":labeler_id} in active_labelers:
        return Status.HTTP_OK, Message.SUCCESS_MESSAGE, project
