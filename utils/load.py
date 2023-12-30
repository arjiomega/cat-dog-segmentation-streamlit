from urllib import request

import cv2
import numpy as np
from PIL import Image

from utils.preprocess import preprocess


def image_from_url(url: str) -> np.ndarray:
    """Load an image from a URL.

    Args:
        url (str): The URL of the image to load.

    Returns:
        numpy.ndarray: The loaded image array.
    """
    response = request.urlopen(url)

    img = np.asarray(bytearray(response.read()), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = preprocess(img, preprocess_list=["resize"], shape=(224, 224))

    return img


def image_from_upload(upload) -> np.ndarray:
    """Load an image from a Streamlit file uploader.

    Args:
        upload: The file uploaded using Streamlit's file_uploader() function.

    Returns:
        numpy.ndarray: The loaded image array.
    """
    img = Image.open(upload)
    img = img.convert("RGB")
    img = np.array(img)
    img = preprocess(img, preprocess_list=["resize"], shape=(224, 224))

    return img
