# Project 4: Multiple choice quiz with input error handling
# Idea: Build a 1-question quiz --> if user types invalid number/string, handle it

try:
    print("❓ What is 2+ 2?")
    print("1) 3\n 2) 4\n 3) 5")

    choice = int(input("Your answer (1-3): "))

    if choice == 2:
        print("✅ Correct!")
    elif choice in [1, 3]:
        print("❌ Wrong answer.")
    else:
        print("❌ Invalid choice.")
except ValueError:
    print("❌ You must enter a number.")

finally:
    print("🎓 Quiz attempt completed.")
