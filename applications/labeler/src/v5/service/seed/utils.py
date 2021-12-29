from src.resources.consts import MONO_SEED, SHARED_SEED
from .SharedLeastLabeledSeed import SharedLeastLabeledSeed
from .MonoSeed import MonoSeed


def get_seed_model(seed_type, meta_model):
    if seed_type == SHARED_SEED:
        return SharedLeastLabeledSeed(meta_model)
    elif seed_type == MONO_SEED:
        return MonoSeed(meta_model)
