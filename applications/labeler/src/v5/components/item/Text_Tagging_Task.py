from ..data.utils import get_data_class
from .TaskObj import TaskObj
from ..data.utils import TextData
from ..label.utils import MultiTags


class Text_Tagging_Task(TaskObj):

    def __init__(self, project_name=None, labeler_id=None, lang=None, _id=None):
        super(TaskObj, self).__init__(project_name, labeler_id, lang, _id)
        self.data_type = TextData
        self.label_type = MultiTags
