# Exercise 2: json_dumps() vs json_dump()

import json

# Python dictionary
user = {
    "username": "c0ff33py",
    "role": "analyst"
}

# Convert dict to Json String
json_str = json.dumps(user)
print(f'JSON: {json_str}')

# Write json to file
with open("user.json", "w") as f:
    json.dump(user, f)

# Comment:
# dumps() = dict -> string
# dump() = dict -> file
