import base64
import io

from PIL import Image


def image_to_base64(image_path):
    img = Image.open(image_path, mode='r')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    return base64.encodebytes(img_byte_arr.getvalue()).decode('ascii')