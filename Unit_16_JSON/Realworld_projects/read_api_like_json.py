import json

# simulated API file
with open("api_users.json", "r") as f:
    data = json.load(f)

# Filter logic
active_users = [u for u in data if u.get("active")]

print("Active users:")
for user in active_users:
    print("-", user["name"])

# Logic:
# Load list of dicts
# Use list comprehension with condition
