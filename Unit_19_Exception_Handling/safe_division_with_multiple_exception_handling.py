# Exercise 3 - Safe Division With multiple Exception Handling

try:
    # Ask user for input
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Try Dividing
    result = num1 / num2
    print(f"✅ Result: {num1} ÷ {num2} = {result}")

except ZeroDivisionError:
    # Handle dividing by zero
    print("❌ Error: Cannot divided by zero.")

except ValueError:
    # Handle if user enter non-integer values
    print("❌ Error: Please enter valid numbers only.")

except Exception as e:
    # Handle any other unexcepted error
    print(f"⚠️ Unexpected Error: {e}")

finally:
    #Always run
    print("👉 Division attempt finished.")
    
    
    
    
    