# nested if

age = 25
citizen = True

# Condition inside another
if age >= 18:
    if citizen:
        print("You can vote.")
    else:
        print("You must be a citizen to vote.")

else:
    print("You are too young to vote.")
