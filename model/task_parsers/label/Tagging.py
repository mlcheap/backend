from .Label import Label
from .consts import TAGGING


class Tagging(Label):

    def __init__(self):
        super(Tagging, self).__init__(TAGGING)
        self.name = "tagging"

    @staticmethod
    def __pars_meta_validation__(json):
        return True

    @staticmethod
    def __pars_validation__(json):
        return True

    def __meta_to_dic__(self):
        return {
            "question": self.question,
            "all-tags": self.all_tags,
            "preferred-tags": self.preferred_tags
        }

    def __label_to_dic__(self):
        return {}

    def __pars_label_json__(self, json):
        pass

    def __pars_meta_json__(self, json):
        self.question = json['question']
        self.all_tags = json['all-tags']
        self.preferred_tags = json['preferred-tags']
