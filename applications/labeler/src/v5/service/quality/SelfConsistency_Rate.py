from .Quality import Quality


class SelfConsistency_Rate(Quality):
    def __init__(self, meta_model):
        super(SelfConsistency_Rate, self).__init__(meta_model)

    @staticmethod
    def __calculate_labeler_quality__(user_id):
        return 1
