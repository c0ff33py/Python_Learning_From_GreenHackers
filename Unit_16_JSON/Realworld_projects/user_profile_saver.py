# Store multiple user profiles in a Json file.
# Add a new user each time script runs

import json
import os

filename = "profiles.json"

# Step 1: Try to load file OR start with empty list

try:
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r") as f:
            users = json.load(f)

    else:
        users = []
except json.JSONDecodeError:
    print("⚠️ profiles.json is corrupted. Starting fresh.")
    users = []

# Step 2: Ask user for new profile data
name = input("Enter your name: ")
age = int(input("Enter your age: "))
role = input("Enter your role: ")

# Step 3: Append new profile to list
new_user = {"name": name, "age": age, "role": role}
users.append(new_user)

# Step 4: Save update user list to file
with open(filename, "w") as f:
    json.dump(users, f, indent=4)

print(f"✅ Profile for ::{name}:: saved successfully.")
