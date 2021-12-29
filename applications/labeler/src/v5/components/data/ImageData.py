from src.resources.consts import IMAGE_DATA
from flask import request
from app import VERSION
from .Data import Data


def get_image_url(image_id):
    return f'{request.url_root}{VERSION}/image?image_id={image_id}'


class ImageData(Data):

    def __init__(self, data_dic=None):
        super(ImageData, self).__init__()
        self.data_type = IMAGE_DATA
        self.__set_data_from_dic__(data_dic)

    def __get_data_json__(self, lang):
        return {
            "im": get_image_url(self.im),
        }

    def __get_data_dic__(self):
        return {
            "im": self.im
        }

    def __set_data__(self, im):
        self.im = im

    def __get_pandas__(self, lang):
        return self.__get_data_dic__()

    def __set_data_from_dic__(self, dic):
        self.im = dic["im"]
