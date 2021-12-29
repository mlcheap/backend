from app import db


def get_task_dbname(project_id):
    return "task_" + project_id


def get_classes_dbname(project_id):
    return "class_" + project_id


def get_class_col(project_id):
    return db[get_classes_dbname(project_id)]


def get_task_col(project_id):
    return db[get_task_dbname(project_id)]


def get_label_col(project_id):
    return db[get_label_dbname(project_id)]


def get_label_dbname(project_id):
    return "label_" + str(project_id)


def get_projects_col():
    return db['projects_db']
