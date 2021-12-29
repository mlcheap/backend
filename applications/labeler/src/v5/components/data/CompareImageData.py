from src.resources.consts import COMPARE_IMAGE_DATA
from flask import request
from app import VERSION
from .Data import Data


def get_image_url(image_id):
    return f'{request.url_root}{VERSION}/image?image_id={image_id}'


class CompareImageData(Data):

    def __init__(self, data_dic):
        im1 = data_dic['im1']
        im2 = data_dic['im2']
        super(CompareImageData, self).__init__()
        self.data_type = COMPARE_IMAGE_DATA
        self.__set_data__(im1, im2)

    def __get_data_json__(self, lang):
        return {
            "im1": get_image_url(self.im1),
            "im2": get_image_url(self.im2)
        }

    def __get_data_dic__(self):
        return {
            "im1": self.im1,
            "im2": self.im2
        }

    def __set_data__(self, im1, im2):
        self.im1 = im1
        self.im2 = im2

    def __get_pandas__(self, lang):
        return self.__get_data_dic__()

    def __set_data_from_dic__(self, dic):
        self.im1 = dic["im1"]
        self.im2 = dic["im2"]
