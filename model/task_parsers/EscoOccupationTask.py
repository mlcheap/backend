from .Task import Task
from .data.consts import ESCO_OCCUPATION_DATA
from .label.consts import ESCO_OCCUPATION_LABEL
from .data import get_data_class
from .label import get_label_class

ESCO_TEXT_TAGGING_TYPE = 'esco-text-tagging'


class EscoOccupationTask(Task):
    task_type = ESCO_TEXT_TAGGING_TYPE
    data_type = ESCO_OCCUPATION_DATA
    label_type = ESCO_OCCUPATION_LABEL

    def __init__(self, items):
        super(EscoOccupationTask, self).__init__(
            EscoOccupationTask.task_type,
            items)

    def __pars_item__(self, item):
        item_obj = None
        if item['name'] == ESCO_OCCUPATION_DATA and item['type'] == "data":
            item_obj = get_data_class(ESCO_OCCUPATION_DATA)()
            item_obj.pars_json(item)
        elif item['name'] == ESCO_OCCUPATION_LABEL and item['type'] == "label":
            item_obj = get_label_class(ESCO_OCCUPATION_LABEL)()
            item_obj.pars_json(item)
        return item_obj
