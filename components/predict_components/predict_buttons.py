import streamlit as st
from streamlit import session_state as ss

from utils.predict import request_predict
from utils import load

import numpy as np


def predict(predict_column):
    match ss.input_type:
        case "image_upload":
            ss.image = load.image_from_upload(ss.input)
        case "video_upload":
            pass
        case "image_url":
            ss.image = load.image_from_url(ss.input)

    if "image" in ss:
        with predict_column:
            with st.spinner("Generating mask..."):
                ss.predict_mask = request_predict(ss.image)


def predict_button(predict_column):
    if "image" not in ss:
        ss.image = None
    if np.any(ss.image):
        disabled = False
    else:
        disabled = True

    st.button(
        "Predict",
        use_container_width=True,
        disabled=disabled,
        on_click=predict,
        args=(predict_column,),
    )
