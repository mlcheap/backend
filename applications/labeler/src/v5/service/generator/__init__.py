from src.resources.consts import RandomCompareGenerator
from .ComparedGenerator import RandomCompareGenerator


def get_generator_model(generated_model, meta_model):
    if generated_model == "RandomCompareGenerator":
        return RandomCompareGenerator(meta_model)
