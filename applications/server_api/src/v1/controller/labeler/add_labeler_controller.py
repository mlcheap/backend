from model.labeler import add_labeler_to_project
from model.customer import find_customer_by_token
from model.cache.query import cache_add_labelers
from model.labeler import find_labeler_id_by_email


def add_labeler_process(project_id, token, emails):
    labeler_ids = set()
    for email in emails:
        labeler_id = find_labeler_id_by_email(email)
        if labeler_id:
            labeler_ids.add(labeler_id)
    customer = find_customer_by_token(token)
    active_labelers, deactivated_labelers = add_labeler_to_project(str(customer["_id"]), project_id, emails)
    # cache_add_labelers(str(customer["_id"]), project_name, list(labeler_ids))
    return active_labelers, deactivated_labelers
