from src.resources.consts import TEXT_DATA, MULTI_CLASS_LABEL, RADIO_LABEL, COMPARE_LABEL
from MultiTagsLabel import MultiTags
from .TextLabel import Text
from .RadioLabel import Radio
from .CompareLabel import Compare


def get_label_class(label_type):
    if label_type == MULTI_CLASS_LABEL:
        return MultiTags
    if label_type == TEXT_DATA:
        return Text
    if label_type == RADIO_LABEL:
        return Radio
    if label_type == COMPARE_LABEL:
        return Compare
