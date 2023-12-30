import cv2
import numpy as np


def resize(array: np.ndarray, shape: tuple[int, int]) -> np.ndarray:
    resized_array = cv2.resize(array, shape, interpolation=cv2.INTER_LINEAR)
    return resized_array


def normalize(array: np.ndarray) -> np.ndarray:
    normalized_array = (array / 127.5) - 1.0
    return normalized_array


def preprocess(array, preprocess_list: list[str], shape: tuple[int, int] = None):
    if "resize" in preprocess_list:
        if shape:
            array = resize(array, shape)
        else:
            raise ValueError("shape is required.")
    if "normalize" in preprocess_list:
        array = normalize(array)

    return array
