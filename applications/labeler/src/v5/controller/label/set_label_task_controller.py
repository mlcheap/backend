from .new_task_controller import new_task_process
from consts import *
from model.labeler import find_labeler_by_id
from model.project import get_labeler_allowed_project
from model.cache.query import cache_label
from model.label import insert_task_labels as insert_label_to_db, exist_label, update_task_labels
from model.task import find_task_by_id, add_labeler_to_task_db
from resources.errors import ApiException


def is_correct_type(part_type, label):
    return True


def send_bad_res(item_objs=None,
                 skip_able=None,
                 total_remain=None,
                 total_labeled=None,
                 message=FAILED_MESSAGE,
                 code=BAD_REQUEST_CODE):
    if item_objs is None:
        item_objs = []
    return item_objs, skip_able, total_remain, total_labeled, message, code


def insert_labels(project_id, labeler_id, task_id, labels, meta_labels, label_time, labels_per_task, lang):
    if exist_label(project_id, str(labeler_id), task_id):
        update_task_labels(project_id, str(labeler_id), task_id, labels, meta_labels, label_time, lang)
    else:
        insert_label_to_db(project_id, str(labeler_id), task_id, labels, meta_labels, label_time, lang)
    add_labeler_to_task_db(project_id, str(labeler_id), task_id, labels_per_task)
    # cache_label(project_name, labeler_id, labeler, task_id)


def exist_task_id(project_id, task_id):
    task = find_task_by_id(project_id, task_id)
    if task:
        return True
    return False


def set_labels_tasks_process(labeler_id, project_id, task, buffer_ids, skipped_ids, lang):
    labeler = find_labeler_by_id(labeler_id)
    project = get_labeler_allowed_project(project_id, labeler, lang)
    if not project:
        return send_bad_res()
    labels_per_task = project["labels_per_task"]
    task_id = task['task_id']
    labels = task['labels']
    if 'meta-labels' in task:
        meta_labels = task['meta-labels']
    else:
        meta_labels = {}

    label_time = task['label_time']
    if exist_task_id(project_id, task_id):
        insert_labels(project_id, labeler_id, task_id, labels, meta_labels, label_time, labels_per_task,
                      lang)
    try:
        new_tasks_objs, stat, message, code = new_task_process(project_id, labeler_id,
                                                               buffer_ids, skipped_ids, lang)
        return new_tasks_objs, stat, message, code

    except ApiException as e:
        return e.response()

