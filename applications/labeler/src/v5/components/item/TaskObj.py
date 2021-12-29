from ..data.utils import get_data_class


class TaskObj:
    def __init__(self, project_name=None, labeler_id=None, lang=None, _id=None, data_type=None, label_type=None):
        self.project_name = project_name
        self.labeler_id = labeler_id
        self.lang = lang
        self._id = _id
        self.data_type = data_type
        self.label_type = label_type
        self.data = None
        self.label = None

    def to_pandas(self):
        item = {}
        if self._id:
            item["_id"] = self._id
        item['lang'] = self.lang
        item['data'] = self.data.to_pandas()
        item['label'] = self.label.to_pandas()
        return item

    def to_json(self):
        item = {}
        if self._id:
            item["_id"] = self._id
        item['lang'] = self.lang
        item['data'] = self.data.to_json(self.lang)
        item['label'] = self.label.to_json(self.lang)
        return item

    def to_db_dic(self):
        item = {}
        if self._id:
            item["_id"] = self._id
        item['lang'] = self.lang
        item['data'] = self.data.to_db_dic()
        item['label'] = self.label.to_db_dic()
        return item

    def pars_data_from_db(self, dic):
        self._id = dic["_id"]
        self.data = get_data_class(self.data_type,
                                   dic["data"])

    def get_data(self):
        return self.data

    def get_label(self):
        return self.label

    def get_lang(self):
        return self.lang

    def pars_label(self, labeler_id, label_json):
        label_json["labeler_id"] = labeler_id
        label_json["project_name"] = self.project_name
        return label_json
