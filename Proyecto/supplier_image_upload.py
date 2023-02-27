import requests
import os


FOLDER = "C:/testpy"
WEBSRVC = "[linux-instance-IP-Address]/upload"
files = os.listdir(FOLDER)


# Iterate though folder
def it_folder():
    for fname in files:
        with open((FOLDER + "/" + fname), "rb") as data_file:
            post_imgs(data_file)


# Where the processment occurs
def process(data_file):
    # TODO Procesar imagenes
    post_imgs()
    pass


# Post images to the webservice
def post_imgs(data):
    requests.post("http://????????/feedback/", files={'file': data})


if __name__ == "__main__":
    pass
