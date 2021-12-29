from app import db


def get_order_project_col():
    return db['order_project']


def exist_label_ordering(project_name):
    col = get_order_project_col()
    return col.find({'project_name': project_name}).count() > 0


def save_ordering(project_name, item_ids, groups):
    col = get_order_project_col()
    col.insert_one({'project_name': project_name, 'item_ids': item_ids, 'groups': groups})


def get_task_orders(project_name):
    col = get_order_project_col()
    return col.find_one({'project_name': project_name})['item_ids']


def get_labeler_groups(project_name):
    col = get_order_project_col()
    return col.find_one({'project_name': project_name})['groups']


def add_labeler_to_mongo_seed(project_name, group, user_id):
    col = get_order_project_col()
    return col.update_one({'project_name': project_name}, {'$push': {f'groups.{group}': user_id}})
