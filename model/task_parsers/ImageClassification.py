from .Task import Task
from .data.consts import IMAGE
from .label.consts import CLASSIFICATION
from .data import get_data_class
from .label import get_label_class


class ImageClassification(Task):
    task_type = 'image-classification'
    data_type = IMAGE
    label_type = CLASSIFICATION

    def __pars_item__(self, item):
        item_obj = None
        if item['name'] == IMAGE and item['type'] == "data":
            item_obj = get_data_class(IMAGE)()
            item_obj.pars_json(item)
        elif item['name'] == CLASSIFICATION and item['type'] == "label":
            item_obj = get_label_class(CLASSIFICATION)()
            item_obj.pars_json(item)
        return item_obj

    def __init__(self, items):
        super(ImageClassification, self).__init__(
            ImageClassification.task_type,
            items)
