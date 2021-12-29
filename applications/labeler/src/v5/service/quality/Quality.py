class Quality:

    def __init__(self, meta_model):
        self.meta_model = meta_model
        self.period_long = meta_model.project.get_quality_period_long()
        self.treshhold_new_items = meta_model.project.get_quality_treshhold_new_items()

    def get_user_quality(self, user_id):
        quality_index = self.meta_model.labels.get_last_quality_update_index(user_id)
        total_labels = self.meta_model.labels.get_total_labels(user_id)
        if total_labels - quality_index >= self.period_long:
            quality = self.__calculate_labeler_quality__(self.meta_model, user_id)
            self.meta_model.labels.update_quality(user_id, total_labels, quality)
        else:
            quality = self.meta_model.labels.get_last_quality_update(user_id)
        return quality

    @staticmethod
    def __calculate_labeler_quality__(meta_model, user_id):
        return 1

    def let_new_items(self, user_id):
        quality = self.get_user_quality(user_id)
        if quality < self.treshhold_new_items:
            return False
        return True
