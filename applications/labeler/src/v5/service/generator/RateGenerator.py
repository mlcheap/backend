from src.v3.service.generator import Generator


class RateGenerator(Generator):

    def __init__(self, meta_model):
        self.meta_model = meta_model

    def generate_new_items(self, user_id, total_need_to_generate):
        return []
