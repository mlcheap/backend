from model.project import find_project_by_id
from model.labeler import find_labeler_by_id
from model.file import find_file_path, exist_file
from consts import OK_CODE, SERVER_ERROR_CODE, SUCCESS_MESSAGE, FAILED_MESSAGE, DEFAULT_ICON_PATH


def project_icon_process(project_id):
    project = find_project_by_id(project_id)
    if project:
        if 'icon_id' in project and exist_file(project['customer_id'], project['icon_id']):
            return find_file_path(project['customer_id'], project['icon_id']), SUCCESS_MESSAGE, OK_CODE
        else:
            return (DEFAULT_ICON_PATH, 'image/gif'), SUCCESS_MESSAGE, OK_CODE

    else:
        return None, FAILED_MESSAGE, SERVER_ERROR_CODE
