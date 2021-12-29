from .consts import CLASSIFICATION, TAGGING, ESCO_OCCUPATION_LABEL
from .Classification import Classification
from .Tagging import Tagging
from .EscoOccupationLabel import EscoOccupationLabel


def get_label_class(label_type):
    if label_type == CLASSIFICATION:
        return Classification
    elif label_type == TAGGING:
        return Tagging
    elif label_type == ESCO_OCCUPATION_LABEL:
        return EscoOccupationLabel
