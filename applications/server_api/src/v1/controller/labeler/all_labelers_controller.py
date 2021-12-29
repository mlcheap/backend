from model.labeler import all_labelers_in_project
from model.customer import find_customer_by_token


def all_labelers_process(project_id, token):
    customer = find_customer_by_token(token)
    active_labelers, deactivated_labelers = all_labelers_in_project(str(customer["_id"]), project_id)
    return active_labelers, deactivated_labelers
