from model.customer import add_customer, find_customer_by_username, \
    save_token, has_token, load_token
from uuid import uuid4


def create_customer_process(username, password):
    customer = find_customer_by_username(username)
    if customer and customer['password'] == password:
        return str(customer["_id"])
    elif not customer:
        add_customer(username, password)
        return str(find_customer_by_username(username)["_id"])


def create_token_process(customer_id):
    if has_token(customer_id):
        return load_token(customer_id)
    rand_token = uuid4()
    save_token(customer_id, str(rand_token))
    return rand_token
