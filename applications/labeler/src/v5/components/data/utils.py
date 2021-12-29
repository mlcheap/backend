from src.resources.consts import IMAGE_DATA, TEXT_DATA, COMPARE_IMAGE_DATA
from .CompareImageData import CompareImageData
from .ImageData import ImageData
from .TextData import TextData


def get_data_class(data_type, data_dic):
    if data_type == COMPARE_IMAGE_DATA:
        return CompareImageData(data_dic)
    if data_type == IMAGE_DATA:
        return ImageData(data_dic)
    if data_type == TEXT_DATA:
        return TextData(data_dic)
