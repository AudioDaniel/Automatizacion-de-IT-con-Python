#!/usr/bin/env python3
import requests
import os


FOLDER = "C:/testpy"
WEBSRVC = "http://" + "[linux-instance-IP-Address]/upload/"
ORIGINAL_FORM = ".jpeg"
files = os.listdir(FOLDER)

# Iterate though folder
def it_folder():
    for fname in files:
        f,extension1 = os.path.splitext(fname)
        if extension1 == ORIGINAL_FORM:
            with open((FOLDER + "/" + fname), "rb") as data_file:
                post_imgs(data_file)


# Post images
def post_imgs(data):
    requests.post(WEBSRVC, files={'file': data})


if __name__ == "__main__":
    it_folder()
