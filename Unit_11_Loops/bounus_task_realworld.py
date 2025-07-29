# 📑 Task: Check attendance from Student list
# Problem:
# - You are given a list of students who attended class today
# - You also have a master list of all students
# - You want to check who missed class.


all_students = {"Alice", "Bob", "Charlie", "David", "Eve"}
attended_students = ["Alice", "Charlie", "Eve"]

# Loop to find absentees
for student in all_students:
    if student not in attended_students:
        print("Absent: ", student)
