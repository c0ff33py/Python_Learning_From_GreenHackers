try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:  # if user input is 0 can cuase error
    print("Can't divided by zero!")
else:
    print("Success! Result =", result)
