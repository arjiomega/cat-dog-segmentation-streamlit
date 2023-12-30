from streamlit_image_select import image_select
from streamlit import session_state as ss

from utils import load


sample_images = [
    "https://t4.ftcdn.net/jpg/00/97/58/97/360_F_97589769_t45CqXyzjz0KXwoBZT9PRaWGHRk5hQqQ.jpg",
    "https://www.hindustantimes.com/ht-img/img/2023/08/25/1600x900/international_dog_day_1692974397743_1692974414085.jpg",
    "https://storage.googleapis.com/petbacker/images/blog/2017/dog-and-cat-cover.jpg",
]

loaded_images = [load.image_from_url(img) for img in sample_images]


def samples(column):
    with column:
        ss.model_input = image_select(
            "Sample Inputs", sample_images, use_container_width=True
        )
