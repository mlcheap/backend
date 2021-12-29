from src.resources.consts import LABEL
from .TextLangs import TextLangs
from abc import abstractmethod
from ..Part import Part


class BaseLabel(Part):

    def __init__(self, name=None, title=None, optional=False):
        self.item_type = LABEL
        self.label_type = None
        self.name = name
        self.optional = optional
        self.title = title
        self.lang = None
        self.user_id = None
        self.response_time = None

    def pars_answer(self, answer=None, lang=None, user_id=None, response_time=None):
        self.lang = lang
        self.user_id = user_id
        self.response_time = response_time
        self.__set_answer__(answer, lang)

    def pars_from_db(self, dic):
        self.name = dic["name"]
        self.optional = dic["label"]["optional"]
        self.title = []
        if "data" in dic["label"]:
            self.__set_data_from_dic__(dic["label"]["data"])
        self.title = TextLangs(dic["label"]["titles"])

    def to_json(self, lang):
        return {
            "label_type": self.label_type,
            "type": self.item_type,
            "name": self.name,
            "label": {
                "optional": self.optional,
                "title": self.title.get_text(lang),
                **self.__get_data_json__(lang)
            }
        }

    def to_db_dic(self):
        return {
            "label_type": self.label_type,
            "type": self.item_type,
            "name": self.name,
            "label": {
                "optional": self.optional,
                "title": self.title.to_db_dic(),
                "data": self.__get_data_dic__()
            }
        }

    def answer_to_dic(self):
        return {
            "name": self.name,
            "answer": self.__get_answer_dic__(),
            "user_id": self.user_id,
            "response_time": self.response_time
        }

    def to_pandas(self, lang):
        pd_dic = self.__get_answer_pandas__(lang)
        return {
            f"{self.name}_lang": lang,
            f"{self.name}_user_id": self.user_id,
            f"{self.name}_response_time": self.response_time
        }.update(
            {f"{self.name}_{key}": pd_dic[key] for key in pd_dic})

    @abstractmethod
    def __set_data_from_dic__(self, dic):
        pass

    @abstractmethod
    def __set_answer__(self, answer, lang):
        pass

    @abstractmethod
    def __set_data__(self, *args):
        pass

    @abstractmethod
    def __get_answer_dic__(self):
        return {}

    @abstractmethod
    def __get_data_json__(self, lang):
        return {}

    @abstractmethod
    def __get_data_dic__(self):
        return {}

    @abstractmethod
    def __get_answer_pandas__(self, lang):
        return {}
