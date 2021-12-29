from app import db
from bson import ObjectId
import datetime
from model.cache.basic import get_labeler_waiting_tasks, count_labeler_mailbox, pop_labeler_mailbox, \
    get_total_unlabeled_tasks, pop_task, add_unique_labelers, add_task_watchers, add_labeler_waiting_task
from model.utils import get_task_col
from model.consts import PENDING, IN_PROGRESS, COMPLETE, CANCELED


def create_task(customer_id, project_id, callbacks, task_dic, unique_id):
    created_at = updated_at = datetime.datetime.utcnow()

    task_db = get_task_col(project_id)

    data_dic = {"project_id": project_id,
                "customer_id": customer_id,
                'created_at': created_at,
                'updated_at': updated_at,
                'callbacks': callbacks,
                'labelers': [],
                'total_labels': 0,
                **task_dic,
                "status": PENDING}
    if unique_id:
        task_db.insert_one({
            **data_dic,
            "_id": ObjectId(unique_id)})
        inserted_id = ObjectId(unique_id)
    else:
        inserted_id = task_db.insert_one(data_dic).inserted_id

    return {
        "_id": str(inserted_id),
        **data_dic,
    }


def find_task(project_id, task_id):
    task_db = get_task_col(project_id)
    return task_db.find_one({"_id": ObjectId(task_id)})


def cancel_task(project_id,
                task_id):
    task_db = get_task_col(project_id)
    task_db.update_one({"_id": ObjectId(task_id)}, {"$set": {"status": CANCELED}})
    return task_db.find_one({"_id": ObjectId(task_id)})


def filter_generation(completed_before, completed_after, created_after, created_before, status):
    filter = {}
    if status:
        filter.update({"status": status})
    if completed_after:
        filter.update({"completed_at": {"$gt": completed_after}})
    return filter


def find_tasks(project_id, completed_before, completed_after,
               created_after, created_before,
               status):
    task_db = get_task_col(project_id)
    query_filter = filter_generation(completed_before, completed_after, created_after, created_before, status)
    return task_db.find({**query_filter}, {"created_at": 1, 'updated_at': 1, 'labelers': 1,
                                           'total_labels': 1, 'task-type': 1, 'status': 1})


def count_tasks(project_id, completed_before, completed_after,
                created_after, created_before,
                status):
    task_db = get_task_col(project_id)
    query_filter = filter_generation(completed_before, completed_after, created_after, created_before, status)
    return task_db.find({**query_filter}).count()


def get_waiting_ids(project_name, labeler_id, total_task):
    waiting_tasks = get_labeler_waiting_tasks(project_name, labeler_id)
    if waiting_tasks:
        return [task.decode('utf-8') for task in list(waiting_tasks)[:total_task]]
    return []


def get_skipped_by_other_users(project_name, labeler_id, total_task):
    tasks = []
    total_mailed_task = count_labeler_mailbox(project_name, labeler_id)
    for i in range(min(total_mailed_task, total_task)):
        tasks.append(pop_labeler_mailbox(project_name, labeler_id))
    return tasks


def get_exist_tasks(project_name, seed, total_need_tasks):
    tasks = []
    total_unlabeled = get_total_unlabeled_tasks(project_name, seed)
    print("total_remain", total_unlabeled, total_need_tasks)
    for i in range(min(total_unlabeled, total_need_tasks)):
        tasks.append(pop_task(project_name, seed).decode("utf-8"))
    return tasks


def catch_send_task_ids(project_name, seed, labeler_id, task_ids):
    add_unique_labelers(project_name, labeler_id)
    add_task_watchers(project_name, seed, task_ids, labeler_id)
    for task_id in task_ids:
        add_labeler_waiting_task(project_name, labeler_id, task_id)


def find_tasks_by_id(project_absname, task_ids):
    task_db = db['task_' + project_absname]
    tasks = list(task_db.find({"_id": {"$in": [ObjectId(id) for id in task_ids]}}))
    for task in tasks:
        task['_id'] = str(task['_id'])
    return tasks


def find_task_by_id(project_id, task_id):
    task_db = get_task_col(project_id)
    return task_db.find_one({"_id": ObjectId(task_id)})


def get_new_tasks_from_db(project_id, labeler_id, buffer_size, buffer_ids, skipped_ids, total_remain_tasks):
    task_db = get_task_col(project_id)
    tasks = list(task_db.find({'_id': {'$nin': [ObjectId(_id) for _id in buffer_ids + skipped_ids]},
                               'status': {'$in': [IN_PROGRESS, PENDING]},
                               'total_labels': {'$lt': buffer_size},
                               'labelers': {'$nin': [labeler_id]}
                               }).sort('total_labels').limit(total_remain_tasks))
    for task in tasks:
        task['_id'] = str(task['_id'])
    return tasks


def add_labeler_to_task_db(project_id, labeler_id, task_id, labels_per_task):
    task_db = get_task_col(project_id)
    task = task_db.find_one({'_id': ObjectId(task_id)})
    total_labels = task['total_labels']
    status = IN_PROGRESS
    if total_labels == labels_per_task:
        status = COMPLETE

    if task:
        labelers = task['labelers'] or []
        labelers.append(labeler_id)
        labelers = list(set(labelers))
        task_db.update_one({'_id': ObjectId(task_id)},
                           {'$set': {
                               'total_labels': len(labelers),
                               'labelers': labelers,
                               "status": status
                           }})


def get_project_total_labeled_labeler(project_id, labeler_id):
    task_db = get_task_col(project_id)
    return task_db.count({'labelers': {"$in": [labeler_id]}})


def get_project_total_remain_labeler(project_id, labeler_id):
    task_db = get_task_col(project_id)
    return task_db.count({'labelers': {"$nin": [labeler_id]}, 'status': {"$nin": [COMPLETE, CANCELED]}})


def get_project_total_tasks_labeled(project_id):
    task_db = get_task_col(project_id)
    return task_db.count({"status": {"$nin": [PENDING, CANCELED]}})


def get_project_total_complete_tasks(project_id):
    task_db = get_task_col(project_id)
    return task_db.count({"status": COMPLETE})


def get_project_total_tasks(project_id):
    task_db = get_task_col(project_id)
    return task_db.count({'status': {"$ne": [CANCELED]}})


def get_project_total_canceled_tasks(project_id):
    task_db = get_task_col(project_id)
    return task_db.count({'status': CANCELED})


def get_labeler_project_stat(project_id, labeler_id):
    return {'total_labeled': get_project_total_labeled_labeler(project_id, labeler_id),
            'total_remain': get_project_total_remain_labeler(project_id, labeler_id)}


def get_project_stat(project_id):
    total_tasks = get_project_total_tasks(project_id)
    total_complete_tasks = get_project_total_complete_tasks(project_id)
    total_tasks_labeled = get_project_total_tasks_labeled(project_id)
    return {"total_tasks": total_tasks,
            "total_complete_tasks": total_complete_tasks,
            "total_tasks_labeled": total_tasks_labeled}


def update_ml_task(project_id, task_id, model_id, results):
    taskdb = get_task_col(project_id)
    task = taskdb.find_one({"_id": ObjectId(task_id)})
    if not "ai" in task:
        task["ai"] = []
    task["ai"].append({"model": model_id, "results": results, "date": datetime.datetime.utcnow()})
    taskdb.update_one({"_id": task_id}, {"$set": {f"ai": task["ai"]}})
    return task
