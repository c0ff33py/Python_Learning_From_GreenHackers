# Creating a dictionary
person = {
    "name": "c0ff33py",
    "age": 30,
    "country": "Myanmar"
}

# Access values using keys
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Add new key-value pair
person['job'] = "Data Engineer"

# Change existing value
person['age'] = 31

# print final dictionary
print("Updated person: ", person)
