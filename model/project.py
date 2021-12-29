from app import db
from resources.errors import CurrentlyExistItem, TokenIsExpired
import datetime
from .customer import find_customer_by_token
from bson import ObjectId
from .consts import LABELS_PER_TASK, COMPLETE, IN_PROGRESS
from .utils import get_task_col, get_projects_col

projects_db = get_projects_col()


def create_project(project_name, customer_id, labels_per_task, icon_id, metadata, model_id):
    created_at = updated_at = datetime.datetime.utcnow()
    if customer_id:
        if projects_db.find_one({'customer_id': customer_id, "project_name": project_name}):
            raise CurrentlyExistItem(param=["project_name"])
        project_id = projects_db.insert_one({
            'created_at': created_at,
            'updated_at': updated_at,
            'customer_id': customer_id,
            LABELS_PER_TASK: labels_per_task,
            "metadata": metadata,
            "icon_id": icon_id,
            "model_id": model_id,
            "project_name": project_name}).inserted_id
        return str(project_id)

    else:
        raise TokenIsExpired


def find_all_projects(customer_token):
    customer = find_customer_by_token(customer_token)
    projects = projects_db.find({'customer_id': str(customer["_id"])})
    return projects


def update_project(project, project_conf):
    projects_db.update_one({'_id': project['_id']},
                           {'$set': project_conf})
    if LABELS_PER_TASK in project_conf:
        new_labels_per_task = project_conf[LABELS_PER_TASK]
        old_labels_per_task = project[LABELS_PER_TASK]
        task_col = get_task_col(str(project['_id']))
        if old_labels_per_task < new_labels_per_task:
            task_col.update({'status': COMPLETE}, {"$set": {'status': IN_PROGRESS}})
        elif old_labels_per_task > new_labels_per_task:
            task_col.update({'status': IN_PROGRESS, 'total_labels': {'$gte': new_labels_per_task}},
                            {"$set": {'status': COMPLETE}})

    return projects_db.find_one({"_id": project["_id"]})


def find_project_by_id(project_id):
    return projects_db.find_one({'_id': ObjectId(str(project_id))})


def get_absolute_project_name(customer_id, project_id):
    return str(customer_id) + "_" + project_id


def get_total_seeds_from_db(customer_id, project_name):
    project = projects_db.find_one({'customer_id': customer_id, "project_name": project_name})
    return project[LABELS_PER_TASK]


def find_permited_projects(labeler, lang):
    projects = list(projects_db.find({'active_labelers': {"$in": [labeler['email']]}}))
    return projects


def get_buffer_size(project_id):
    return 1


def get_quality_treshhold(project):
    return 0.8


def get_labeler_allowed_project(project_id, labeler, lang):
    allowed_projects = find_permited_projects(labeler, lang)
    for proj in allowed_projects:
        if str(proj['_id']) == project_id:
            return proj
    return None


# def get_customer_allowed_project(project_id, customer_id):
#     allowed_projects = find_permited_projects(labeler, lang)
#     for proj in allowed_projects:
#         if str(proj['_id']) == project_id:
#             return proj
#     return None


def get_labels_per_task(project_id):
    return find_project_by_id(project_id)[LABELS_PER_TASK]
