import requests


def is_upload_image(image_upload):
    file_type = image_upload.type.split("/")[0]

    if file_type == "image":
        return True
    else:
        return False


def is_url_image(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    if r.headers["content-type"] in image_formats:
        return True
    else:
        return False