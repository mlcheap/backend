from src.resources.consts import TEXT_TAGGING_TASK
from .Text_Tagging_Task import Text_Tagging_Task


def get_task_class(data_type, data_dic):
    if task_type == TEXT_TAGGING_TASK:
        return Text_Tagging_Task(data_dic)
