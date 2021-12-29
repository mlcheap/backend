from abc import abstractmethod


class Data:

    def __init__(self, data_type):
        self.data_type = data_type

    @staticmethod
    @abstractmethod
    def __pars_validation__(json):
        pass

    @abstractmethod
    def __to_dict__(self):
        return {}

    def to_dict(self):
        data_dic = self.__to_dict__()
        return {'data-type': self.data_type, "data": data_dic, "name": self.name, "type": "data"}

    @abstractmethod
    def __pars_json__(self, json):
        pass

    def pars_json(self, json):
        if not self.__pars_validation__(json):
            return False, "not validate data"
        self.__pars_json__(json)
        return True, ""
