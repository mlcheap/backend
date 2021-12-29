from src.resources.consts import BAD_REQUEST_CODE, OK_CODE, SUCCESS_MESSAGE, USER_NOT_EXIST_MASSAGE
from src.v3.model.labeler import  delete_labeler, find_labeler_by_email
from app import blacklist


def delete_user_process(email):
    user = find_labeler_by_email(email)
    if not user:
        return USER_NOT_EXIST_MASSAGE, BAD_REQUEST_CODE

    blacklist.add(user.id)
    # delete_user_labels(labeler)
    delete_labeler(user)

    return SUCCESS_MESSAGE, OK_CODE
