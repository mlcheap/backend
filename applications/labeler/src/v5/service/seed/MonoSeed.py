from src.v3.service.seed.Seed import Seed


class MonoSeed(Seed):
    def __init__(self, meta_model):
        super(MonoSeed, self).__init__(meta_model)

    @staticmethod
    def __create_seed_for_user__(meta_model, user_id):
        seed_id = meta_model.label.get_total_group() + 1
        # self.meta_model.label.set_user_group(user_id, group)
        # self.meta_model.label.add_group_user(group, user_id)
        # self.meta_model.add_user_to_mongo_group(group, user_id)
        return int(seed_id)
