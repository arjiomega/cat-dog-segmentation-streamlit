import json
import urllib
import requests

import cv2
import numpy as np

from utils.preprocess import preprocess


def request_predict(image: np.ndarray):
    image = preprocess(image, preprocess_list=["normalize"])
    image = np.expand_dims(image, axis=0)

    payload = json.dumps({"inputs": image.tolist()})
    headers = {"Content-Type": "application/json"}
    endpoint_url = "http://127.0.0.1:5000/invocations"

    response = requests.post(endpoint_url, data=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
    else:
        print("Failed to get a prediction. Status code:", response.status_code)

    result = response.json()
    predict_mask = np.array(result["predictions"][0])

    return predict_mask
