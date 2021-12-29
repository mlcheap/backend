from app import rdb


def tasks_key(project_dbname, seed):
    return f'{project_dbname}:{seed}:tasks'


def total_tasks_key(project_dbname):
    return f'{project_dbname}:total_tasks'


def task_labelers_key(project_dbname, task_id):
    return f'{project_dbname}:{task_id}:labelers'


def labeler_waiting_task_key(project_dbname, labeler_id):
    return f'{project_dbname}:{labeler_id}:waiting'


def total_seeds_key(project_dbname):
    return f'{project_dbname}:total_seeds'


def total_labeled_key(project_dbname):
    return f'{project_dbname}:total_labeled'


def total_labeler_labeled_key(project_dbname, labeler_id):
    return f'{project_dbname}:{labeler_id}:total_labeled'


def total_labelers_score_key():
    return f'total_score'


def db_labelers_score_key(project_dbname):
    return f'{project_dbname}:score'


def unique_labeled_tasks_key(project_dbname):
    return f'{project_dbname}:unique_labeled_tasks'


def unique_labelers_key(project_dbname):
    return f'{project_dbname}:unique_labelers'


def labeler_seed_key(project_dbname, labeler_id):
    return f'{project_dbname}:{labeler_id}:seed'


def tasks_seen_key(project_dbname, seed, task_id):
    return f'{project_dbname}:{seed}:{task_id}:tasks_seen'


def seed_labelers_key(project_dbname, seed):
    return f'{project_dbname}:{seed}:seed_labelers'


def labeler_mailbox_key(project_dbname, labeler_id):
    return f'{project_dbname}:{labeler_id}:mailbox'


def inc_labeler_total_labeled(project_dbname, labeler_id):
    return rdb.incr(total_labeler_labeled_key(project_dbname, labeler_id), 1)


def inc_project_labeler_score(project_dbname, labeler_id):
    rdb.zincrby(db_labelers_score_key(project_dbname), 1, labeler_id)


def inc_total_labeler_score(labeler_id):
    rdb.zincrby(total_labelers_score_key(), 1, labeler_id)


def add_task_labeled(project_dbname, task_id, labeler_id):
    rdb.sadd(task_labelers_key(project_dbname, task_id), labeler_id)


def add_labeler_waiting_task(project_dbname, labeler_id, task_id):
    rdb.sadd(labeler_waiting_task_key(project_dbname, labeler_id), task_id)


def rem_labeler_waiting_task(project_dbname, labeler_id, task_id):
    rdb.srem(labeler_waiting_task_key(project_dbname, labeler_id), task_id)


def add_to_labeler_mailbox(project_dbname, labeler_id, task_id):
    rdb.lpush(labeler_mailbox_key(project_dbname, labeler_id), task_id)


def pop_task(project_dbname, seed):
    if rdb.llen(tasks_key(project_dbname, seed)) > 0:
        return rdb.lpop(tasks_key(project_dbname, seed))


def count_labeler_mailbox(project_dbname, labeler_id):
    return rdb.llen(labeler_mailbox_key(project_dbname, labeler_id))


def pop_labeler_mailbox(project_dbname, labeler_id):
    if count_labeler_mailbox(project_dbname, labeler_id) > 0:
        return rdb.lpop(labeler_mailbox_key(project_dbname, labeler_id))


def count_task_labeled(project_dbname, task_id):
    return rdb.scard(task_labelers_key(project_dbname, task_id))


def set_total_seeds(project_dbname, total_seeds):
    return rdb.set(total_seeds_key(project_dbname), total_seeds)


def delete_total_seeds(project_dbname):
    return rdb.delete(total_seeds_key(project_dbname))


def set_total_tasks(project_dbname, total_tasks):
    print(total_tasks_key(project_dbname))
    return rdb.set(total_tasks_key(project_dbname), total_tasks)


def get_total_tasks(project_dbname):
    total_tasks = rdb.get(total_tasks_key(project_dbname))
    if total_tasks:
        return int(total_tasks)
    return 0


def get_total_seeds(tasks_dbname):
    return int(rdb.get(total_seeds_key(tasks_dbname)))


def get_seeds_remain(project_dbname):
    seed_remains = []
    for seed in range(get_total_seeds(project_dbname)):
        seed_remains.append(get_total_unlabeled_tasks(project_dbname, seed))
    return seed_remains


def add_labeler_to_seed(project_dbname, labeler_id, seed):
    return rdb.sadd(seed_labelers_key(project_dbname, seed), labeler_id)


def remove_labeler_from_seed(project_dbname, labeler_id, seed):
    print('srem', seed_labelers_key(project_dbname, seed), labeler_id)
    rdb.srem(seed_labelers_key(project_dbname, seed), labeler_id)


def get_seed_labelers(project_dbname, seed):
    return rdb.smembers(seed_labelers_key(project_dbname, seed))


def get_seeds_labelers(project_dbname):
    seeds_labelers = []
    for seed in get_all_seeds(project_dbname):
        seeds_labelers.append(
            [seed_labeler.decode('utf-8') for seed_labeler in get_seed_labelers(project_dbname, seed)])
    return seeds_labelers


def set_seed_labelers(project_dbname, seed, labeler_ids):
    return rdb.sadd(seed_labelers_key(project_dbname, seed), *labeler_ids)


def add_task_watchers(project_dbname, seed, task_id, labeler_id):
    return rdb.sadd(tasks_seen_key(project_dbname, seed, task_id), labeler_id)


def get_task_seens(project_dbname, seed, task_id):
    return rdb.smembers(tasks_seen_key(project_dbname, seed, task_id))


def get_labeler_total_labeled(project_dbname, labeler_id):
    return rdb.get(total_labeler_labeled_key(project_dbname, labeler_id))


def get_task_labelers(project_dbname, task_id):
    return rdb.smembers(task_labelers_key(project_dbname, task_id))


def get_total_unlabeled_tasks(project_dbname, seed):
    return rdb.llen(tasks_key(project_dbname, seed))


def get_project_scores(project_dbname):
    return rdb.zrevrangebyscore(db_labelers_score_key(project_dbname), '+inf', '-inf')


def get_total_scores():
    return rdb.zrevrangebyscore(total_labelers_score_key(), '+inf', '-inf')


def insert_tasks_to_seed(project_dbname, seed_name, remain_tasks):
    if len(remain_tasks) > 0:
        rdb.rpush(tasks_key(project_dbname, seed_name), *remain_tasks)


def add_unique_labeled_tasks(project_dbname, taskids):
    return rdb.sadd(unique_labeled_tasks_key(project_dbname), taskids)


def get_total_unique_labeled_tasks(project_dbname):
    return rdb.scard(unique_labeled_tasks_key(project_dbname))


def add_unique_labelers(project_dbname, labelerids):
    return rdb.sadd(unique_labelers_key(project_dbname), *labelerids)


def get_total_unique_labelers(project_dbname):
    return rdb.scard(unique_labelers_key(project_dbname))


def set_labeler_seed(project_dbname, labeler_id, seed):
    print(labeler_seed_key(project_dbname, labeler_id), seed)
    return rdb.set(labeler_seed_key(project_dbname, labeler_id), seed)


def delete_labeler_seed(project_dbname, labeler_id):
    return rdb.delete(labeler_seed_key(project_dbname, labeler_id))


def get_labeler_seed(project_dbname, labeler_id):
    return rdb.get(labeler_seed_key(project_dbname, labeler_id))


def exist_in_labeler_waiting_list(project_dbname, labeler_id, task_id):
    return rdb.sismember(labeler_waiting_task_key(project_dbname, labeler_id), task_id)


def get_labeler_waiting_tasks(project_dbname, labeler_id):
    return rdb.smembers(labeler_waiting_task_key(project_dbname, labeler_id))


def rem_task_from_seed(project_dbname, seed, task_id):
    return rdb.lrem(tasks_key(project_dbname, seed), task_id)


def remove_project_catch(project_dbname):
    for key in rdb.scan_iter(f"{project_dbname}:*"):
        rdb.delete(key)


def incr_total_labeled(project_dbname):
    return rdb.incr(total_labeled_key(project_dbname))


def get_total_labeled(project_dbname):
    if rdb.exists(total_labeled_key(project_dbname)):
        tb = rdb.get(total_labeled_key(project_dbname))
        if tb:
            return int(tb)
        return 0
    return 0


def get_all_seeds(project_absname):
    return range(get_total_seeds(project_absname))


def get_project_score(project_name, labeler_id):
    score = rdb.zscore(db_labelers_score_key(project_name), labeler_id)
    if score:
        return score
    return 0


def get_project_rank(project_name, labeler_id):
    rank = rdb.zrank(db_labelers_score_key(project_name), labeler_id)
    if rank:
        return rank
    total_num = rdb.zcard(db_labelers_score_key(project_name))
    if total_num:
        return total_num
    return 1


def get_total_rank(labeler_id):
    rank = rdb.zrank(total_labelers_score_key(), labeler_id)
    if rank:
        return rank
    return 9999


def get_total_score(labeler_id):
    score = rdb.zscore(total_labelers_score_key(), labeler_id)
    if score:
        return score
    return 0
