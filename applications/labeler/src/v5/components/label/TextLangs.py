from src.resources.consts import ENGLISH_LANG


class TextLangs:
    def __init__(self, text_langs):
        self.text_langs = text_langs

    def to_dic(self):
        return self.text_langs

    def get_text(self, lang):
        text = None
        for text_lang in self.text_langs:
            if text_lang["lang"] == lang:
                return text_lang["title"]
            if text_lang["lang"] == ENGLISH_LANG:
                title = text_lang["title"]
        if text:
            return text
        if len(self.text_langs) > 0:
            return self.text_langs[0]["title"]
