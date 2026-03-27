import json
import os

FILE_PATH = "data/passwords.json"

def load_passwords():
    if not os.path.exists(FILE_PATH):
        return {}

    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except:
        return {}


def save_passwords(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)
