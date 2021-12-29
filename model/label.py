from bson import ObjectId
from .utils import get_label_col, get_task_col
from .consts import IN_PROGRESS
from datetime import datetime


def find_labelers_tasks_labels(project_id):
    label_col = get_label_col(project_id)
    return list(label_col.aggregate([{"$group": {"_id": "$labeler_id", "task_ids": {"$addToSet": "$task_id"}}}]))


def find_all_labeler_task_ids(project_id):
    label_col = get_label_col(project_id)
    return list(label_col.find({}, {"labeler_id": 1, "task_id": 1, "_id": -1}))


def insert_task_labels(project_id, user_id, task_id, labels, meta_labels, label_time, lang):
    label_col = get_label_col(project_id)
    label_col.insert_one(
        {'labeler_id': user_id, 'task_id': task_id,
         'labels': labels, "meta_labels": meta_labels, 'lang': lang, 'inserted_at': datetime.utcnow(),
         'label_time': label_time})


def update_task_labels(project_id, labeler_id, task_id, labels, meta_labels, label_time, lang):
    label_col = get_label_col(project_id)
    label_col.update_one(
        {'labeler_id': labeler_id, 'task_id': task_id}, {'$set': {
            'labels': labels, "meta_labels": meta_labels, 'lang': lang, 'updated_at': datetime.utcnow(),
            'label_time': label_time}})


def exist_label(project_id, labeler_id, item_id):
    label_col = get_label_col(project_id)
    return label_col.count({'labeler_id': labeler_id, 'task_id': item_id})


def get_project_total_labels(project_id):
    label_col = get_label_col(project_id)
    return label_col.count()


def find_task_labels(project_id, task_id):
    label_col = get_label_col(project_id)
    return label_col.find({'task_id': task_id})
