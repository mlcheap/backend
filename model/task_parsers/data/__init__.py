from .consts import IMAGE, TEXT, ESCO_OCCUPATION_DATA
from .Image import Image
from .Text import Text
from .EscoOccupationData import EscoOccupationData


def get_data_class(data_type):
    if data_type == IMAGE:
        return Image
    elif data_type == TEXT:
        return Text
    elif data_type == ESCO_OCCUPATION_DATA:
        return EscoOccupationData
