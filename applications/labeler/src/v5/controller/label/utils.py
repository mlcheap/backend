from model.cache.query import get_seed
from model.task import get_waiting_ids, get_skipped_by_other_users, get_exist_tasks, catch_send_task_ids


def get_new_task_ids(project_name, labeler_id, buffer_ids, total_need_tasks):
    print('total_need_tasks', total_need_tasks)
    waiting_ids = get_waiting_ids(project_name, labeler_id, total_need_tasks)
    print('waiting_ids', waiting_ids)
    task_ids = list(set(waiting_ids).difference(buffer_ids))

    mail_task_ids = get_skipped_by_other_users(project_name, labeler_id, total_need_tasks - len(task_ids))
    print('mail_task_ids', mail_task_ids)
    task_ids += mail_task_ids

    seed = get_seed(project_name, labeler_id)
    print(total_need_tasks, task_ids)
    total_need_tasks = total_need_tasks - len(task_ids)
    print(total_need_tasks)
    print('seed', seed)
    new_tasks = get_exist_tasks(project_name, seed, total_need_tasks)

    print('new_tasks', new_tasks)
    task_ids += new_tasks

    if len(task_ids) > 0:
        catch_send_task_ids(project_name, seed, labeler_id, task_ids)

    return task_ids
