from abc import abstractmethod


class Label:

    def __init__(self, label_type):
        self.label = None
        self.label_type = label_type

    @staticmethod
    @abstractmethod
    def __pars_validation__(json):
        pass

    @staticmethod
    @abstractmethod
    def __pars_meta_validation__(json):
        pass

    @abstractmethod
    def __meta_to_dic__(self):
        pass

    @abstractmethod
    def __label_to_dic__(self):
        pass

    def to_dict(self):
        dic = {"meta-label": self.__meta_to_dic__(),
               'label-type': self.label_type,
               "name": self.name,
               "type": "label"}
        if self.label:
            dic.update({"label": self.__label_to_dic__()})
        return dic

    @abstractmethod
    def __pars_label_json__(self, json):
        pass

    @abstractmethod
    def __pars_meta_json__(self, json):
        pass

    def pars_json(self, json):
        self.name = json['name']
        self.__pars_meta_json__(json['meta-label'])
        return True, ""
