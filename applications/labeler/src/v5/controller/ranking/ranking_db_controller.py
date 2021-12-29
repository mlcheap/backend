from consts import OK_CODE, SUCCESS_MESSAGE
from model.cache.basic import get_project_scores, get_project_rank


def get_rank_with_score(fdbname, min, max):
    ss = get_project_scores(fdbname, min, max)
    return [{'labeler': ss[i][0].decode('utf-8').split('_', 1)[0], 'score': int(ss[i][1]), 'rank': i + min + 1} for i in
            range(len(ss))]


def ranking_db_process(user_id, fdbname, lang):
    top_range = 20
    around_margin = 3
    rank = get_project_rank(fdbname, user_id)
    if rank <= top_range + around_margin:
        ranks = get_rank_with_score(fdbname, 0, max(top_range, rank + around_margin))
        if len(ranks) == 0:
            return rank, [rank], SUCCESS_MESSAGE, OK_CODE
        return rank, ranks, SUCCESS_MESSAGE, OK_CODE
    else:
        top_billboard = get_rank_with_score(fdbname, 0, top_range)
        arround_billboard = get_rank_with_score(fdbname, rank - around_margin, rank + around_margin)
        return rank, top_billboard + arround_billboard, SUCCESS_MESSAGE, OK_CODE
