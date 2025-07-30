# Project 2: Login Attempt Tracker with error log
# idea: User login system --> if login fails, log the error to `login.log`

from datetime import datetime
# Predefined account info
valid_user = "c0ff33py"
valid_pass = "greenbean123"

try:
    username = input("Username: ")
    password = input("Password: ")

    if username != valid_user or password != valid_pass:
        raise ValueError("Invalid credentials.")

    print("✅ Login successful!")

except ValueError as e:
    print("❌ Login Failed:", e)
    with open("login.log", "a") as log:
        log.write(f"[{datetime.now()}] Failed login: {username}\n")
finally:
    print("🔐 Login attempt recorded.")
