# Exercise 1: Division calculator with exception handling

try: 
    # User input for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Division operation
    restult = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {restult}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed. Please enter a non-zero second number.")
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")

finally:
    # Always run

    print("Thank you for using the division calculator.")