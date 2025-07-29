try:
    num = int(input("Enter number: "))
    print("100 / num =", 100 / num)

except ValueError:
    print("Invalid input! Please enter numbers only.")

except ZeroDivisionError:
    print("You can't divide by zero!")

except Exception as e:
    print("An error occurred:", e)
