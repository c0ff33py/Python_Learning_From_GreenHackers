# Grading Example
marks = int(input("Enter your mark: "))

if marks > 100 or marks < 0:
    print("Invalid mark.")
elif marks >= 90:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 70:
    print("C Grade")
else:
    print("Fail")
