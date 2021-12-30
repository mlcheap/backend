from Exceptions.AuthExceptions import UserNotExistsException
from model.project import find_permited_projects
from model.task import get_labeler_project_stat
# from src.v5.model.redis.basic import get_total_rank, get_total_score
# from src.v5.model.redis.query import get_userinfo_for_score
from model.labeler import find_labeler_by_id, get_total_rank, get_total_score
from flask import request
from .....app import VERSION


def add_icon(projects):
    for project in projects:
        project['icon'] = f'{request.url_root}api/{VERSION}/file/icon?project_id={str(project["_id"])}'

    return projects


def add_stat(projects, labeler_id):
    for project in projects:
        stat = get_labeler_project_stat(str(project["_id"]), str(labeler_id))
        for key in stat:
            project[key] = stat[key]
    return projects


def init_process(lang, labeler_id):
    labeler = find_labeler_by_id(labeler_id)
    if not labeler:
        raise UserNotExistsException

    allowed_projects = find_permited_projects(labeler, lang)
    projects = add_stat(allowed_projects, labeler_id)
    projects = add_icon(projects)
    total_rank = get_total_rank(labeler_id)
    total_score = get_total_score(labeler_id)
    rank_info = {"rank": total_rank, "score": total_score}
    return labeler, projects, rank_info
