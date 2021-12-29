from .basic import *
from model.project import get_absolute_project_name, get_total_seeds_from_db
from model.labeler import get_labeler_seed_from_db, set_labeler_seed_to_db, \
    delete_labeler_seed_from_db, get_labelers_seed_from_db
from model.label_order import add_labeler_to_mongo_seed
import random


def cache_create_project(project_name, customer_id, total_seeds):
    tasks_dbname = get_absolute_project_name(customer_id, project_name)
    set_total_seeds(tasks_dbname, total_seeds)


def cache_tasks_seed(project_absname, task_ids, seed):
    total_task = get_total_tasks(project_absname)
    set_total_tasks(project_absname, total_task + len(task_ids))
    # total_seeds = get_total_seeds(project_absname)
    # if seed >= total_seeds:
    #     set_total_seeds(project_absname, seed + len(task_ids))
    insert_tasks_to_seed(project_absname, seed, task_ids)


def cache_tasks(customer_id, project_name, task_ids):
    project_absname = get_absolute_project_name(customer_id, project_name)
    seeds = get_all_seeds(project_absname)
    for seed in seeds:
        cache_tasks_seed(project_absname, task_ids, seed)


def delete_cache_task(customer_id, project_name, task_id):
    seeds = get_all_seeds(project_name)
    for seed in seeds:
        delete_cache_tasks_seed(customer_id, project_name, task_id, seed)


def delete_cache_tasks_seed(customer_id, project_name, task_id, seed):
    project_absname = get_absolute_project_name(customer_id, project_name)
    total_task = get_total_tasks(project_absname)
    set_total_tasks(project_absname, total_task - 1)
    rem_task_from_seed(project_absname, seed, task_id)


def cache_add_labelers(customer_id, project_name, labeler_ids):
    project_absname = get_absolute_project_name(customer_id, project_name)
    for labeler_id in labeler_ids:
        cache_add_labeler(project_absname, labeler_id)


def least_remain_least_labelers(indexes, seeds_remain, seeds_users):
    irus = zip(indexes, seeds_remain, seeds_users)
    irus = sorted(irus, key=lambda iru: (-iru[1], len(iru[2])))
    return irus[0]


def cache_add_labeler(project_absname, labeler_id):
    if labeler_id:
        seed = get_labeler_seed(project_absname, labeler_id)
        print('seed1', seed)
        if seed:
            return seed

        seed = get_labeler_seed_from_db(project_absname, labeler_id)
        print('seed2', seed)
        if seed:
            set_labeler_seed(project_absname, labeler_id, seed)
            add_labeler_to_seed(project_absname, labeler_id, seed)
            return seed
        print('seed3', seed)

        seeds_remain = get_seeds_remain(project_absname)
        indexes = list(range(len(seeds_remain)))
        seeds_users = get_seeds_labelers(project_absname)
        print(indexes, seeds_remain, seeds_users)
        seed = least_remain_least_labelers(indexes, seeds_remain, seeds_users)[0]
        print('seed4', seed)

        set_labeler_seed(project_absname, labeler_id, seed)
        add_labeler_to_seed(project_absname, labeler_id, seed)
        set_labeler_seed_to_db(project_absname, labeler_id, seed)

        return int(seed)


def cache_cancel_labeler(customer_id, project_name, labeler_id):
    project_absname = get_absolute_project_name(customer_id, project_name)
    if labeler_id:
        seed = get_labeler_seed(project_absname, labeler_id)
        if seed:
            delete_labeler_seed(project_absname, labeler_id)
            print(project_absname, labeler_id, seed)
            remove_labeler_from_seed(project_absname, labeler_id, seed.decode('utf-8'))
            print('delete_labeler_seed_from_db', project_absname, labeler_id, seed.decode('utf-8'))
            delete_labeler_seed_from_db(project_absname, labeler_id, seed.decode('utf-8'))


def cache_remove_seed(project_absname, seed):
    pass


def cache_labeler(customer_id, project_name, labeler, seed):
    pass


def cache_reset(customer_id, project_name):
    project_absname = get_absolute_project_name(customer_id, project_name)
    seeds = get_all_seeds(project_absname)
    for seed in seeds:
        cache_remove_seed(project_absname, seed)
    delete_total_seeds(project_absname)
    total_seeds = get_total_seeds_from_db(customer_id, project_name)
    set_total_seeds(project_absname, total_seeds)
    labelers_seed = get_labelers_seed_from_db(project_absname)
    for seed in labelers_seed:
        for labeler in labelers_seed:
            cache_labeler(customer_id, project_name, labeler, seed)


def get_seed_with_maximum_remain_tasks(project_name):
    seeds_remain = get_seeds_remain(project_name)
    indexes = list(range(len(seeds_remain)))
    seeds_labelers = get_seeds_labelers(project_name)
    irus = zip(indexes, seeds_remain, seeds_labelers)
    irus = sorted(irus, key=lambda iru: (-iru[1], len(iru[2])))
    return irus[0][0]


def get_seed(project_name, labeler_id):
    seed = get_labeler_seed(project_name, labeler_id)
    if seed:
        return int(seed)

    # seed = get_db_labeler_seed(project_name, labeler_id)
    # if seed != -1:
    #     return seed

    seed = get_seed_with_maximum_remain_tasks(project_name)

    set_labeler_seed(project_name, labeler_id, seed)
    add_labeler_to_seed(project_name, seed, labeler_id)
    add_labeler_to_mongo_seed(project_name, seed, labeler_id)
    return int(seed)


def get_unseens_tasks(project_name, seed, task_id):
    labelers_id = get_seed_labelers(project_name, seed)
    seens_id = get_task_seens(project_name, seed, task_id)
    return list(set(labelers_id).difference(set(seens_id)))


def add_waiting_ids(project_name, labeler_id, skipped_ids):
    seed = get_seed(project_name, labeler_id)
    for old_id in skipped_ids:
        add_task_watchers(project_name, seed, old_id, labeler_id)
        rem_labeler_waiting_task(project_name, labeler_id, old_id)
        unseen_labelers = get_unseens_tasks(project_name, seed, old_id)
        if len(unseen_labelers) > 0:
            unseen_labeler = random.sample(unseen_labelers, 1)[0]
            add_to_labeler_mailbox(project_name, unseen_labeler, old_id)


def cache_label(project_name, labeler_id, labeler, task_id):
    if exist_in_labeler_waiting_list(project_name, labeler_id, task_id):
        seed = get_seed(project_name, labeler_id)
        add_task_watchers(project_name, seed, task_id, labeler_id)
    add_unique_labeled_tasks(project_name, task_id)
    inc_labeler_total_labeled(project_name, labeler_id)
    # inc_project_labeler_score(project_name, get_labelerinfo_for_score(labeler))
    # inc_total_labeler_score(get_labelerinfo_for_score(labeler))
    rem_labeler_waiting_task(project_name, labeler_id, task_id)
    add_task_labeled(project_name, task_id, labeler_id)
    incr_total_labeled(project_name)


def get_labelerinfo_for_score(labeler):
    return labeler['name'] + '_' + str(labeler['_id'])
