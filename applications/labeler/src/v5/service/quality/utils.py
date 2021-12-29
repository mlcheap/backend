from src.resources.consts import SELF_CONSISTENCY_COMPARE, SELF_CONSISTENCY_RATE
from .SelfConsistency_Rate import SelfConsistency_Rate
from .SelfConsistency_Compare import SelfConsistency_Compare


def get_quality_model(quality_type,meta_model):
    if quality_type == SELF_CONSISTENCY_COMPARE:
        return SelfConsistency_Compare(meta_model)
    elif quality_type == SELF_CONSISTENCY_RATE:
        return SelfConsistency_Rate(meta_model)
