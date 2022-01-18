from typing import IO
# Dict, Generator, Generic, List, TypeVar, Union
from .Api import Api
from .env import *


class Client:
    def __init__(self,
                 api_key):
        self.api = Api(api_key=api_key)

    def predict(self,  task_dic):
        return self.api.post_request(f'top-tags', body=task_dic)

    def get_class_info(self, lang, class_dic):
        return self.api.post_request(f'get-occupation', body=class_dic)
