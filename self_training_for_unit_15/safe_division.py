# Project 1: Safe Division Calculator
# Ask user for 2 inputs and safelfy divide

try:
    num1 = int(input("Pls enter numerator: "))  # Top number
    num2 = int(input("Pls enter denominator: "))  # Bottom number

    result = num1 / num2  # Actual division
    print(f'Result: {result}')

except ZeroDivisionError:
    print("❌ cannot divide by Zero.")
except ValueError:
    print("❌ Please enter only numbers.")
except Exception as e:
    print("❌ Unexpected error: ", str(e))
finally:
    print("Division attempt completed.")
