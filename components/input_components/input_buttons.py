from streamlit import session_state as ss

from utils import expectations, load


def clicked_button1():
    ss.button1 = True
    ss.button2 = False
    ss.button3 = False

    ss.image = None
    ss.predict_mask = None


def clicked_button2():
    ss.button1 = False
    ss.button2 = True
    ss.button3 = False

    ss.image = None
    ss.predict_mask = None


def clicked_button3():
    ss.button1 = False
    ss.button2 = False
    ss.button3 = True

    ss.image = None
    ss.predict_mask = None


def load_input(column):
    predict_input = None
    input_type = None

    if ss.button1:
        input_ = column.file_uploader("Upload Image for Prediction")

        if input_:
            if expectations.is_upload_image(input_):
                predict_input = input_
                input_type = "image_upload"
            else:
                column.error("Uploaded file must be an image.")

    if ss.button2:
        # do not accept if image_url does not contain an image
        input_ = column.text_input("Image URL")

        if input_:
            if expectations.is_url_image(input_):
                predict_input = input_
                input_type = "image_url"
            else:
                column.error(f"Image url does not contain an image.")

    if ss.button3:
        predict_input = ss.model_input
        input_type = "image_samples"

    return predict_input, input_type


def input_buttons(column):
    col1, col2, col3 = column.columns(3)
    col1.button("upload image", on_click=clicked_button1, use_container_width=True)
    col2.button("use image url", on_click=clicked_button2, use_container_width=True)
    col3.button("use sample image", on_click=clicked_button3, use_container_width=True)

    if "button1" and "button2" and "button3" not in ss:
        ss.button1, ss.button2, ss.button3 = None, None, None

    ss.input, ss.input_type = load_input(column)

    if ss.input and ss.input_type:
        match ss.input_type:
            case "image_upload":
                ss.image = load.image_from_upload(ss.input)
                column.success("Image successfully loaded. You can now press predict.")
            case "image_url":
                ss.image = load.image_from_url(ss.input)
                column.success("Image successfully loaded. You can now press predict.")
            case "image_samples":
                ss.image = load.image_from_url(ss.input)
                column.success(
                    "Sample image successfully loaded. You can now press predict."
                )
