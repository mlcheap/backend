from model.project import find_project_by_id
from model.labeler import all_labelers_in_project, find_labeler_by_id
from resources.helpers import Status, Message
from model.classes import find_classes


def get_all_classes_process(labeler_id,
                      project_id):
    project = find_project_by_id(project_id)
    lang = project['lang']
    labeler = find_labeler_by_id(labeler_id)
    customer_id = project["customer_id"]
    active_labelers, deactivated_labelers = all_labelers_in_project(customer_id, project_id)
    if {"email": labeler['email'], "_id": labeler_id} in active_labelers:
        return find_classes(project_id)
