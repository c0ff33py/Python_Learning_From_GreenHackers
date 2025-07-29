# Scope

x = 10  # Global variable


def show():
    x = 5  # local variable
    print("Inside: ", x)


show()
print("Outside:", x)
