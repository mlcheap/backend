from src.resources.consts import DATA
from abc import abstractmethod
from ..Part import Part


class Data(Part):

    def __init__(self):
        self.item_type = DATA
        self.data = None
        self.data_type = None

    def pars_data_from_db(self, dic):
        self.__set_data_from_dic__(dic)

    def to_json(self, lang):
        return {
            "data_type": self.data_type,
            "type": self.item_type,
            "data": self.__get_data_json__(lang)
        }

    def to_db_dic(self):
        return {
            "data_type": self.data_type,
            "type": self.item_type,
            "data": self.__get_data_dic__()
        }

    def to_pandas(self, lang):
        pd_dic = self.__get_pandas__(lang)
        return {f"data_{key}": pd_dic[key] for key in pd_dic}

    @abstractmethod
    def __set_data__(self, *args):
        pass

    @abstractmethod
    def __get_pandas__(self, lang):
        pass

    @abstractmethod
    def __set_data_from_dic__(self, dic):
        pass

    @abstractmethod
    def __get_data_json__(self, lang):
        pass

    @abstractmethod
    def __get_data_dic__(self):
        return {}
