from .BaseLabel import BaseLabel


class Compare(BaseLabel):

    def __init__(self, name=None, title=None, optional=False):
        super(Compare, self).__init__(name, title, optional)
        self.answer = False

    def __set_answer__(self, answer, lang):
        self.answer = answer

    def __set_data_from_dic__(self, dic):
        pass

    def __set_data__(self, data):
        pass

    def __get_answer_dic__(self):
        return {"label": self.answer}

    def __get_answer_pandas__(self, lang):
        return self.__get_answer_dic__()

    def __get_data_json__(self, lang):
        return {}

    def __get_data_dic__(self):
        return {}
