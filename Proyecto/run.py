#! /usr/bin/env python3

import os
import requests

DIRECTORY = "supplier-data/descriptions/"
WEBSRVC = "linux-instance-IP-Address/fruits"

FBACK_DICT = {
    "name": "",
    "weigh": "",
    "description": "",
    "image_name": "",
}


files = os.listdir(FOLDER)


def it_folder():
    for fname in files:
        with open(FOLDER + "/" + fname) as data_file:
            process(data_file)


def process(data_file):
    i = 0
    for line in data_file:
        it_dictionary(line, i)
        i += 1
    post_fback(FBACK_DICT)


def it_dictionary(line, i):
    ln_no_nwline = line.rstrip()
    keys = list(FBACK_DICT.keys())
    FBACK_DICT[keys[i]] = ln_no_nwline


def post_fback(data):
    requests.post("http://????????/feedback/", data)


if __name__ == "__main__":
    it_folder()
