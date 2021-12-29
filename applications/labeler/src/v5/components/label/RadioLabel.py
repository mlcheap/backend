from BaseLabel import BaseLabel


class TagRails:
    def __init__(self, lang=None, tags=None):
        self.lang = lang
        self.tags = tags

    def to_dic(self):
        return {"lang": self.lang, "tags": self.tags}


class Radio(BaseLabel):

    def __init__(self, name=None, title=None, optional=False):
        super(Radio, self).__init__(name, title, optional)
        self.answer = ""
        self.all = {}

    def __set_answer__(self, answer, lang):
        self.answer = answer

    def __set_data__(self, tag_rails):
        self.all = tag_rails

    def __set_data_from_dic__(self, data):
        for lang in data:
            self.all[lang] = TagRails(lang, data[lang]["all"])

    def __get_answer_dic__(self):
        return {"answer": self.answer}

    def __get_data_json__(self, lang):
        return {"all_labels": self.all[lang].to_db_dic()}

    def __get_data_dic__(self):
        data = {}
        for lang in self.all:
            data[lang] = {"all": self.all[lang].to_db_dic()}
        return data

    def __get_answer_pandas__(self, lang):
        return self.__get_answer_dic__()
