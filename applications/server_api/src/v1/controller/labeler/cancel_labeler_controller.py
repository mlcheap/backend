from model.labeler import cancel_labeler_from_project
from model.customer import find_customer_by_token
from model.cache.query import cache_cancel_labeler
from model.labeler import find_labeler_id_by_email


def cancel_labeler_process(project_id, token, email):
    # labeler_id = find_labeler_id_by_email(email)
    customer = find_customer_by_token(token)
    active_labelers, deactivated_labelers = cancel_labeler_from_project(str(customer["_id"]), project_id, email)
    # cache_cancel_labeler(str(customer["_id"]), project_name, labeler_id)
    return active_labelers, deactivated_labelers
