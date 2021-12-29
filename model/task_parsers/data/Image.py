from .Data import Data
from .consts import IMAGE


class Image(Data):
    def __init__(self):
        super(Image, self).__init__(IMAGE)

    @staticmethod
    def __pars_validation__(json):
        return True

    def __to_dict__(self):
        return {"file-id": self.file_id}

    def __pars_json__(self, json):
        self.file_id = json["data"]['file_id']
        self.name = json["name"]
