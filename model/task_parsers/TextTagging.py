from .Task import Task
from .data.consts import TEXT
from .label.consts import TAGGING
from .data import get_data_class
from .label import get_label_class


class TextTagging(Task):
    task_type = 'text-tagging'
    data_type = TEXT
    label_type = TAGGING

    def __pars_item__(self, item):
        item_obj = None
        print(item)
        if item['name'] == TEXT and item['type'] == "data":
            item_obj = get_data_class(TEXT)()
            item_obj.pars_json(item)
        elif item['name'] == TAGGING and item['type'] == "label":
            item_obj = get_label_class(TAGGING)()
            item_obj.pars_json(item)
        return item_obj

    def __init__(self, items):
        super(TextTagging, self).__init__(
            TextTagging.task_type,
            items)
