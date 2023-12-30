import streamlit as st
from streamlit import session_state as ss


from .input_components import input_buttons, samples
from .predict_components import predict_window, predict_buttons


def input_column_components(input_column):
    input_column.header("Input")
    samples.samples(input_column)
    input_buttons.input_buttons(input_column)


def predict_column_components(predict_column):
    predict_column.header("Predict")
    predict_window.window_prediction(predict_column)
    predict_buttons.predict_button(predict_column)


def body():
    input_column, predict_column = st.columns(2)

    input_column_components(input_column)
    predict_column_components(predict_column)
