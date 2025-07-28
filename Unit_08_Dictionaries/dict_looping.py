# dict_looping
data = {
    "Python": "Win Htut",
    "Linux": "c0ff33py",
    "Git": "Green Hackers"
}

# Loop through keys
for key in data:
    print("Course: ", key)

# Loop through values
for value in data.values():
    print("Instructor: ", value)

# Loop through both key and value
for key, value in data.items():
    print(f"{key} is taught by {value}")
