from src.v3.service.seed.Seed import Seed


class SharedLeastLabeledSeed(Seed):

    def __init__(self, meta_model):
        super(SharedLeastLabeledSeed, self).__init__(meta_model)

    @staticmethod
    def __create_seed_for_user__(meta_model, user_id):
        total_seeds = meta_model.label.get_total_seeds()
        if total_seeds < meta_model.project.get_max_seeds():
            return int(total_seeds) + 1

        seed_id = meta_model.label.get_most_remain_tasks_seed()
        return int(seed_id)
