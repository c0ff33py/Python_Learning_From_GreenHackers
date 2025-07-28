person = {
    "name": "c0ff33py",
    "age": 30
}

# Get value safely (return None if key doesn't exist)
print(f"City: {person.get('city')}")

# Update multiple keys at once
person.update({'age': 31, "city": "Yangon"})

# Remove key
person.pop("age")
print("final: ", person)
