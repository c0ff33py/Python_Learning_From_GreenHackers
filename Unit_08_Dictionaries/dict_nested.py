# dictionary nested

students = {
    "stu01": {"name": "Aye Aye", "grade": "A"},
    "stu02": {"name": "Myo Myo", "grade": "B"}
}

# Access nested value
print("Stu01 name: ", students["stu01"]["name"])

# Loop all students
for sid, info in students.items():
    print(f"{sid} - {info['name']} got {info['grade']}.")
