from .Label import Label
from .consts import CLASSIFICATION


class Classification(Label):

    def __init__(self):
        super(Classification, self).__init__(CLASSIFICATION)

    @staticmethod
    def __pars_meta_validation__(json):
        return True

    @staticmethod
    def __pars_validation__(json):
        return True

    def __meta_to_dic__(self):
        return {
            "question": self.question,
            "classes": self.classes
        }

    def __label_to_dic__(self):
        return {}

    def __pars_label_json__(self, json):
        pass

    def __pars_meta_json__(self, json):
        self.question = json['question']
        self.classes = json['classes']
