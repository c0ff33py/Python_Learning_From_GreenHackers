#  Project 5: Age Checker with Validation + File Logging
# Idea: Ask user for their age --> check if valid --> log error if invalid
# Use case: Real-world forms always need input validation & logging

from datetime import datetime

try:
    age = int(input("Enter your age: "))

    if age <= 0 or age > 120:
        raise ValueError("Unrealitstic age.")

    print(f'You are {age} years old.')

except ValueError as e:
    print("❌ Invalid age:", e)
    with open("age_errors.log", "a") as log:
        log.write(f"[{datetime.now()}] Invalid age input: {age}\n")

finally:
    print("Age check complete.")
