#!/usr/bin/env python3
from os import listdir, path
from unicodedata import normalize
import requests
import json


txt_dir = "supplier-data/descriptions/"


text_files = [txt_dir + f for f in listdir(txt_dir) if f.endswith(".txt")]


def getEntry(file):
    
    entry_id = path.splitext(path.basename(file))[0]
    img_name = entry_id + ".jpeg"

    with open(file) as f:
        lines = f.read().strip().splitlines()
    name, weight, description = lines

    weight = int(weight.replace(" lbs", ""))

  
    keys = ["name", "weight", "description", "image_name"]
    vals = [name, weight, description, img_name]
    entry = dict(zip(keys, vals))
    return entry


url = "http://localhost/fruits/"
for file in text_files:
    data = getEntry(file)
    response = requests.post(url, data=data)
    if response.ok:
        print("uploaded data")
    else:
        print(f"error: {response.status_code}")
