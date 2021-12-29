from abc import abstractmethod
from src.v3.model.redis.basic import get_user_exist_group, \
    user_have_group


class Seed:
    def __init__(self, meta_model):
        self.meta_model = meta_model

    @staticmethod
    @abstractmethod
    def __create_seed_for_user__(meta_model, user_id):
        return -1

    def get_user_seed(self, user_id):
        if user_have_group(self.meta_model.project.project_name, user_id):
            return get_user_exist_group(self.meta_model.project.project_name, user_id)
        seed_id = self.__create_seed_for_user__(self.meta_model, user_id)
        self.meta_model.label.set_new_user_seed(user_id, seed_id)
        return seed_id
