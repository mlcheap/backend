from src.v1.model.labeler import add_labeler_to_project
from src.v1.model.customer import find_customer_by_token
from src.v1.model.cache.query import cache_add_labelers


def reset_cache_process(project_name, token, email):
    customer = find_customer_by_token(token)
    cache_reset(str(customer["_id"]), project_name, email)

