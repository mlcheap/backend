from src.resources.consts import TEXT_DATA
from .Data import Data
from ..label.TextLangs import TextLangs


class TextData(Data):

    def __init__(self,  text_langs=None):
        super(TextData, self).__init__()
        self.data_type = TEXT_DATA
        self.__set_data_from_dic__(text_langs)

    def get_text(self, lang):
        return self.text_langs.get_text(lang)

    def __get_data_json__(self, lang):
        text = self.get_text(lang)
        return {
            "text": text
        }

    def __get_data_dic__(self):
        return self.text_langs.to_dic()

    def __set_data__(self, text_langs):
        self.text_langs = text_langs

    def __get_pandas__(self, lang):
        return {"text": self.get_text(lang)}

    def __set_data_from_dic__(self, dic):
        self.text_langs = TextLangs(dic)
