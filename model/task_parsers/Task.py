from abc import abstractmethod


class Task:

    def __init__(self, task_type, items):
        self.task_type = task_type
        self.items = items
        self.items_obj = []
        for item in items:
            item_obj = self.__pars_item__(item)
            self.items_obj.append(item_obj)

    @abstractmethod
    def __pars_item__(self, item):
        pass

    # def pars_json(self):
    #     data_status, data_message =
    #     if not data_status:
    #         return False, data_message
    #
    #     label_status, label_message =
    #     if not label_status:
    #         return False, label_message
    #     return True, ""

    def to_dict(self):
        items_dic = []
        for item_obj in self.items_obj:
            item_dic = item_obj.to_dict()

            items_dic.append(item_dic)
        # data_item.update({'type': 'data', 'name': self.data_obj.name})
        # label_item = self.label_obj.to_dict()
        # label_item.update({'type': 'label', 'name': self.label_obj.name})
        return {
            "task-type": self.task_type,
            "items": items_dic
        }
