from consts import OK_CODE, SUCCESS_MESSAGE
from model.label import find_labeler_labeled_tasks_base_time
from model.project import find_permited_projects
from model.labeler import find_labeler_by_id


def get_total_days(all_tasks):
    return 5


def get_total_projects(all_tasks):
    return 2


def get_total_hours(all_tasks):
    return 3


def get_report_unit_time(total_days):
    return "day"


def get_daily_reports(all_tasks):
    return {"june 20": {'labels': 20, 'hours': 30}, "june 21": {'labels': 18, 'hours': 38}}


def report_process(labeler_id, _from, to):
    report = {}
    labeler = find_labeler_by_id(labeler_id)
    projects = find_permited_projects(labeler, "en")
    all_tasks = []
    for project in projects:
        tasks = find_labeler_labeled_tasks_base_time(labeler_id, str(project["_id"]), _from, to)
        all_tasks += tasks
    total_hours = get_total_hours(all_tasks)
    total_projects = get_total_projects(all_tasks)
    total_days = get_total_days(all_tasks)
    report['stats'] = {'total_hours': total_hours, 'total_projects': total_projects, 'total_days': total_days}

    report_unit_time = get_report_unit_time(total_days)
    if report_unit_time == "day":
        daily_reports = get_daily_reports(all_tasks)
        report['details'] = daily_reports

    return report, SUCCESS_MESSAGE, OK_CODE
