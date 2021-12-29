# from . import ImageClassification, TextTagging, EscoOccupationTask
from .TextTagging import TextTagging
from .ImageClassification import ImageClassification
from .EscoOccupationTask import EscoOccupationTask


def get_task_class(task_type):
    if task_type == ImageClassification.task_type:
        return ImageClassification
    if task_type == TextTagging.task_type:
        return TextTagging
    if task_type == EscoOccupationTask.task_type:
        return EscoOccupationTask


def task_parser(task_type, items):
    task_class = get_task_class(task_type)
    return task_class(items)
