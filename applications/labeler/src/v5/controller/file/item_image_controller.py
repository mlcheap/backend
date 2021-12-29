from consts import OK_CODE, SERVER_ERROR_CODE, SUCCESS_MESSAGE, FAILED_MESSAGE
from model.file import find_file_path


def image_process(path):
    im_path = find_file_path(path)
    if im_path:
        return im_path, SUCCESS_MESSAGE, OK_CODE
    return None, FAILED_MESSAGE, SERVER_ERROR_CODE
    # infodb = find_info_by_dbname(dbname)
    # if infodb:
    #     item = find_item_by_id(dbname, item_id)
    #     item_type = get_part_types(infodb, [part_name])[0]
    #     model_class = get_model_class('data', item_type)
    # item_path = model_class.get_item_path(item['data_' + part_name + '_part'], key)
    # return item_path, SUCCESS_MESSAGE, OK_CODE
    # else:
    # return None, FAILED_MESSAGE, SERVER_ERROR_CODE
