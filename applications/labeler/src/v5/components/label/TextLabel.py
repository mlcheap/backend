from src.resources.consts import TEXT_LABEL
from BaseLabel import BaseLabel


class Text(BaseLabel):

    def __init__(self, name=None, titles=None, optional=None):
        super(Text, self).__init__(name, titles, optional)
        self.label_type = TEXT_LABEL

    def __set_data_from_dic__(self, dic):
        pass

    def __set_answer__(self, answer, lang):
        pass

    def __set_data__(self, data):
        pass

    def __get_answer_dic__(self):
        pass

    def __get_data_json__(self, lang):
        pass

    def __get_data_dic__(self):
        pass

    def __get_answer_pandas__(self, lang):
        pass
