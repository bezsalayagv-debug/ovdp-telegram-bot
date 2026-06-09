import json
import os

FILE = "data.json"


def load():
    if not os.path.exists(FILE):
        return []
    return json.load(open(FILE))


def save(data):
    json.dump(data, open(FILE, "w"))
