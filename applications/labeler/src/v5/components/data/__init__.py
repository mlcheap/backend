from src.resources.consts import IMAGE_DATA, TEXT_DATA, COMPARE_IMAGE_DATA
from .ImageData import ImageData
from .CompareImageData import CompareImageData
from .TextData import TextData


def get_data_component(component_name):
    if component_name == IMAGE_DATA:
        return ImageData
    if component_name == COMPARE_IMAGE_DATA:
        return CompareImageData
    if component_name == TEXT_DATA:
        return TextData
