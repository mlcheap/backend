from consts import OK_CODE, SUCCESS_MESSAGE
from model.labeler import find_labeler_by_id
from model.project import find_permited_projects
from model.cache.basic import get_total_rank, get_total_score, get_project_score, get_project_rank
from model.cache.query import get_labelerinfo_for_score


def ranking_info_process(user_id, lang):
    user = find_labeler_by_id(user_id)
    user_key = get_labelerinfo_for_score(user)
    dbs_info = find_permited_projects(user, lang)
    total_rank = get_total_rank(user_key)
    total_score = get_total_score(user_key)
    db_ranks = []
    total_info = {'total_rank': total_rank, 'total_score': total_score}
    for db in dbs_info:
        dbname = db['dbname']
        db_rank_info = get_db_info(dbname, user_key)
        title = dbname.rsplit('_', 1)[0]
        db_ranks.append({'dbname': dbname, 'title': title, **db_rank_info})
    return db_ranks, total_info, SUCCESS_MESSAGE, OK_CODE


def get_db_info(dbname, user_key):
    return {'score': get_project_score(dbname, user_key), 'rank': get_project_rank(dbname, user_key)}
