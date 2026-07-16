import json
import os
from datetime import date

DATA_FILE = "water_data.json"


def load_data():

    if not os.path.exists(DATA_FILE):
        return {
            "date": str(date.today()),
            "count": 0,
            "goal": 8
        }

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    # Reset automatically every new day
    if data["date"] != str(date.today()):
        data["date"] = str(date.today())
        data["count"] = 0

    return data


def save_data(data):

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def drink_water():

    data = load_data()
    data["count"] += 1
    save_data(data)


def get_count():

    return load_data()["count"]


def get_goal():

    return load_data()["goal"]


def reset_today():

    data = load_data()
    data["count"] = 0
    save_data(data)