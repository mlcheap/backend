from model.project import create_project
# from model.cache import cache_create_project
from model.customer import find_customer_by_token
from consts.consts import OK_CODE, SUCCESS_MESSAGE, BAD_REQUEST_CODE, FAILED_MESSAGE


def create_project_process(project_name, customer_token, labels_per_task, icon_id, metadata, model_id):
    customer = find_customer_by_token(customer_token)
    print('salam')
    if customer:
        print("customer")
        customer_id = str(customer["_id"])
        project_id = create_project(project_name, customer_id, labels_per_task, icon_id, metadata, model_id)
        # cache_create_project(project_name, customer_id, labels_per_task)
        print("okey code")
        return OK_CODE, SUCCESS_MESSAGE, project_id
    else:
        print(BAD_REQUEST_CODE, "back request")
        return BAD_REQUEST_CODE, FAILED_MESSAGE, None
