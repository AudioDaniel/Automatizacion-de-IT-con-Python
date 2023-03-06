from PIL import Image
import os

IMAGE_SIZE = 600, 400
DIRECTORY = "/home/audiodev/Programacion/Mis-Scripts-de-Python/Proyecto/Imgs"
TARGET_DIR = "/home/audiodev/Programacion/Mis-Scripts-de-Python/Proyecto/Imgs"
FORMAT = ".jpeg"
ORIGINAL_FORM = ".tiff"

def img_processor():
    files = []
    for f in os.listdir(DIRECTORY):
        fname = DIRECTORY + "/" + f
        fname1,extension1 = os.path.splitext(f)
        if os.path.isfile((fname)) and extension1 == ORIGINAL_FORM:
            files.append(fname)

    for imgpath in files:
        resize_image(imgpath)


def resize_image(imgpath):
    with Image.open(imgpath) as im:
        im = im.convert("RGB")
        im.thumbnail(IMAGE_SIZE)
        basename = os.path.basename(imgpath)
        fname1,extension1 = os.path.splitext(basename)
        full_target_dir = TARGET_DIR + "/" + basename + "resize"
        im.save(full_target_dir + FORMAT)


if __name__ == "__main__":
    img_processor()
