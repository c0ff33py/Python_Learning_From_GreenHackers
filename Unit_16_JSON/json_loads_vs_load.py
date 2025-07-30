# Exercise 1: json.loads(), json.load()

import json

# JSON string (text format)
json_string = '{"name":"c0ff33py", "age":30}'

# convert json string to Python dictionary
data = json.loads(json_string)

print("Username: ", data["name"])
print("Age:", data["age"])

# Comment:
# json.loads() is for string-based JSON(from API, etc.)
