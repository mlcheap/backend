from .BaseLabel import BaseLabel


class Tags():
    def __init__(self, lang=None, tags=None):
        self.lang = lang
        self.tags = tags

    def to_dic(self):
        return {"lang": self.lang, "tags": self.tags}


class MultiTags(BaseLabel):

    def __init__(self, name=None, title=None, optional=False):
        super(MultiTags, self).__init__(name, title, optional)
        self.answer = Tags()
        self.original = {}
        self.predicted = {}
        self.all = {}

    def __set_answer__(self, tags, lang):
        self.answer = Tags(lang, tags)

    def __set_data__(self, all_tags, original_tags, predicted_tag):
        self.all = all_tags
        self.original = original_tags
        self.predicted = predicted_tag

    def __set_data_from_dic__(self, data):
        for lang in data:
            self.all[lang] = Tags(lang, data[lang]["all"])
            self.original[lang] = Tags(lang, data[lang]["original"])
            self.predicted[lang] = Tags(lang, data[lang]["predicted"])

    def __get_answer_dic__(self):
        return {"answer": self.answer.to_dic()}

    def __get_answer_pandas__(self, lang):
        return {"answer": self.answer.to_dic()["tags"]}

    def __get_data_json__(self, lang):
        return {"all_labels": self.all[lang].to_db_dic(),
                "original": self.original[lang].to_db_dic(),
                "predicted": self.predicted[lang].to_db_dic()}

    def __get_data_dic__(self):
        data = {}
        for lang in self.all:
            data[lang] = {"all": self.all[lang].to_db_dic(),
                          "original": self.original[lang].to_db_dic(),
                          "predicted": self.predicted[lang].to_db_dic()}

        return data
