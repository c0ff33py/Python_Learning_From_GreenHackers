#  Dictionary in list

people = [
    {"name": "Alice", "job": "Developer"},
    {"name": "Bob", "job": "Designer"},
    {"name": "Charlie", "job": "Manager"}
]

# Loop through list of dicts
for person in people:
    print(f"{person['name']} is a {person['job']}")
