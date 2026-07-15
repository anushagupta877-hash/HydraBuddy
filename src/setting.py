import json
import os

SETTINGS_FILE = os.path.join(
    os.path.dirname(__file__),
    "..",
    "settings.json"
)

DEFAULT_SETTINGS = {
    "daily_goal": 8,
    "reminder_interval": 30
}


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        save_settings(DEFAULT_SETTINGS)
        return DEFAULT_SETTINGS

    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)