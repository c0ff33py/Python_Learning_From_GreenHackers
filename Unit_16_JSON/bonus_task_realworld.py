import json
from datetime import datetime


def load_config(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        with open("error.log", "a") as log:
            log.write(f"[{datetime.now()}] Failed to load {filename}:{e}\n ")
        return {"username": "default_user", "debug": False}


# Try to load config
config = load_config("config.json")

print("User:", config["username"])
print("Debug mode:", config["debug"])
