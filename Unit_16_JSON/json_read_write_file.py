# Exercise 3 :
import os
import json


filename = "user.json"

# check if file exists first
if os.path.exists(filename):
    with open(filename, "r") as f:
        user_data = json.load(f)
else:
    # If file doesn't exist, create with default data
    user_data = {"username": "c0ff33py", "role": "Data analyt"}
    with open(filename, "w") as f:
        json.dump(user_data, f)
    print("Create new user.json with default data.")

# Add a new key and write back
user_data["active"] = True

with open(filename, "w") as f:
    json.dump(user_data, f)

print("Updated user.json: ", user_data)
# comment:
# json.load() = file -> dict
# file update require overwrite
