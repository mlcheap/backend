from .Label import Label
from .consts import ESCO_OCCUPATION_LABEL


class EscoOccupationLabel(Label):

    def __init__(self):
        super(EscoOccupationLabel, self).__init__(ESCO_OCCUPATION_LABEL)
        self.name = "esco-occupation-label"

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
            "ai": self.ai
        }

    def __label_to_dic__(self):
        return {}

    def __pars_label_json__(self, json):
        pass

    def __pars_meta_json__(self, json):
        self.question = json['question']
        self.all_tags = json['all-tags']
        if 'ai' in json:
            self.ai = json['ai']
        else:
            self.ai = []
