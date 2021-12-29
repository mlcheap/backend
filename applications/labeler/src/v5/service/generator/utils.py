from .RateGenerator import RateGenerator
from .ComparedGenerator import CompareGenerator


def get_generator_model(generator_policy, meta_model):
    if generator_policy == "rate":
        return RateGenerator(meta_model)
    if generator_policy == "compare":
        return CompareGenerator(meta_model)
