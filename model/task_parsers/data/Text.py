from .Data import Data
from .consts import TEXT


class Text(Data):
    def __init__(self):
        super(Text, self).__init__(TEXT)

    @staticmethod
    def __pars_validation__(json):
        return True

    def __to_dict__(self):
        return {"text": self.text}

    def __pars_json__(self, json):
        self.text = json["data"]['text']
        self.name = json['name']
