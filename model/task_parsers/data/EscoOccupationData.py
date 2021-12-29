from .Data import Data
from .consts import ESCO_OCCUPATION_DATA


class EscoOccupationData(Data):

    def __init__(self):
        super(EscoOccupationData, self).__init__(ESCO_OCCUPATION_DATA)

    @staticmethod
    def __pars_validation__(json):
        return True

    def __to_dict__(self):
        return {"title": self.title, "description": self.description}

    def __pars_json__(self, json):
        self.title = json["data"]['title']
        self.description = json["data"]['description']
        self.name = json['name']
