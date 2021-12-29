from consts import BAD_REQUEST_CODE, OK_CODE, SUCCESS_MESSAGE, FAILED_MESSAGE
from model.project import get_buffer_size, get_labeler_allowed_project, find_project_by_id
from model.task import get_new_tasks_from_db, get_labeler_project_stat, update_ml_task
from model.quality import get_quality
from model.project import get_quality_treshhold
from model.labeler import find_labeler_by_id
from Exceptions.AuthExceptions import UserNotExistsException, ProjectNotExistException
from model.task_parsers import task_parser
from .ai_predict_controller import ai_predict_process


# from model.cache.query import add_waiting_ids


def fail_response():
    return [], {}, FAILED_MESSAGE, BAD_REQUEST_CODE


def have_condition(project_name, user_id):
    return True


# def get_new_tasks_from_cache(project_name, labeler_id, buffer_size, skipped_ids, buffer_ids):
#     add_waiting_ids(project_name, labeler_id, skipped_ids)
#     total_remain_tasks = buffer_size - len(buffer_ids)
#     task_ids = get_new_task_ids(project_name, labeler_id, buffer_ids, total_remain_tasks)
#     status = {}
#     if len(task_ids) == 0:
#         return [], status, SUCCESS_MESSAGE, OK_CODE
#     tasks = find_tasks_by_id(project_name, [task_id for task_id in task_ids])
#     return tasks, status, SUCCESS_MESSAGE, OK_CODE

def convert_tasks_front_format(tasks):
    tasks_front_format = []
    for task in tasks:
        print('task', task['items'][1]['meta-label'])
        tff = task_parser(task['task-type'], task['items']).to_dict()
        tff.update({"task_id": str(task["_id"]), 'skip_able': False})
        tasks_front_format.append(tff)
    return tasks_front_format


def get_new_tasks(project_id, labeler_id, buffer_size, skipped_ids, buffer_ids):
    total_remain_tasks = buffer_size - len(buffer_ids)

    tasks = get_new_tasks_from_db(project_id, str(labeler_id), buffer_size, buffer_ids, skipped_ids,
                                  total_remain_tasks)
    project = find_project_by_id(project_id)
    for task in tasks:
        if "model_id" in project and project["model_id"] != "":
            task['items'][1]['meta-label']["ai"] = ai_predict_process(labeler_id, project_id, str(task["_id"]), excludes=[])
    tasks_front_format = convert_tasks_front_format(tasks)
    stat = get_labeler_project_stat(project_id, str(labeler_id))
    if len(tasks_front_format) == 0:
        return [], stat, SUCCESS_MESSAGE, OK_CODE

    return tasks_front_format, stat, SUCCESS_MESSAGE, OK_CODE


def new_task_process(project_id, labeler_id, buffer_ids, skipped_ids, lang):
    labeler = find_labeler_by_id(labeler_id)
    if not labeler:
        raise UserNotExistsException

    project = get_labeler_allowed_project(project_id, labeler, lang)
    if not project:
        raise ProjectNotExistException

    if not have_condition(project, labeler_id):
        return fail_response()

    quality = get_quality(project, labeler_id)
    if quality < get_quality_treshhold(project):
        return fail_response()

    buffer_size = get_buffer_size(project_id)
    # tasks, status, SUCCESS_MESSAGE, OK_CODE = get_new_tasks_from_cache(project_name,
    #                                                                labeler_id,
    #                                                                buffer_size,
    #                                                                skipped_ids,
    #                                                                buffer_ids)
    tasks, stat, SUCCESS_MESSAGE, OK_CODE = get_new_tasks(project_id,
                                                          labeler_id,
                                                          buffer_size,
                                                          skipped_ids,
                                                          buffer_ids)

    return tasks, stat, SUCCESS_MESSAGE, OK_CODE
