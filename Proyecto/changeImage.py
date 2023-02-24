from PIL import Image
import os

IMAGE_SIZE = 600, 400
DIRECTORY = "J:/Git/Mis-Scripts-de-Python/Proyecto/Imgs"
TARGET_DIR = "J:/Git/Mis-Scripts-de-Python/Proyecto/Imgs/Thmbnails"
FORMAT = ".jpeg"


def img_processor():
    files = []
    for f in os.listdir(DIRECTORY):
        fname = DIRECTORY + "/" + f
        if os.path.isfile((fname)):
            files.append(fname)

    for imgpath in files:
        resize_image(imgpath, f)


def resize_image(imgpath, f):
    with Image.open(imgpath) as im:
        im.convert("RGB")
        im.thumbnail(IMAGE_SIZE)
        full_target_dir = TARGET_DIR + "/" + f + "resize"
        im.save(full_target_dir + FORMAT)


if __name__ == "__main__":
    img_processor()
