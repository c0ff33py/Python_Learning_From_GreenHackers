import json
from datetime import datetime


def load_config(filename="config.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)

    except (FileNotFoundError, json.JSONDecodeError):
        # log and fallback
        with open("config_error.log", "a") as log:
            log.write(f"[{datetime.now()}] Failed to load {filename}\n")
        return {"theme": "dark", "autosave": True}


config = load_config()
print("Theme:", config["theme"])
