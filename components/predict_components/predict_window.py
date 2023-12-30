import numpy as np
from streamlit import session_state as ss


def image_predict_pair(image_col, predict_col):
    image_col.image(ss.image)
    predict_col.image(ss.predict_mask)


def window_prediction(column):
    image_col, predict_col = column.columns(2)

    if "predict_mask" not in ss:
        ss.predict_mask = None

    if np.any(ss.predict_mask):
        image_predict_pair(image_col, predict_col)
