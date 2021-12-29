from abc import abstractmethod


class Part:
    @abstractmethod
    def to_pandas(self, lang):
        pass

    @abstractmethod
    def to_json(self, lang):
        pass

    @abstractmethod
    def to_db_dic(self):
        pass
