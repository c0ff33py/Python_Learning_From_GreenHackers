# Json_list_dict

import json

# List of dictionaries
people = [
    {"name": "Alice", "job": "Data Analyst"},
    {"name": "Bob", "job": "Engineer"}
]

# Converted to Json String
json_people = json.dumps(people)
print("People Json:", json_people)

# Save to file
with open("people.json", "w") as f:
    json.dump(people, f)

# Comment: JSON is very common for storing list of records
