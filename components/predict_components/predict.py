import streamlit as st
from streamlit import session_state as ss


from utils import load
from utils.predict import request_predict


def predict(predict_column):
    match ss.input_type:
        case "image_upload":
            ss.image = load.image_from_upload(ss.input)
        case "video_upload":
            pass
        case "image_url":
            ss.image = load.image_from_url(ss.input)

    with predict_column:
        with st.spinner("Generating mask..."):
            ss.predict_mask = request_predict(ss.image)
