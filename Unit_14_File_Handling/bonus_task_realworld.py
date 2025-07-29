from datetime import datetime

log_message = f"[{datetime.now()}] User logged in.\n"

with open("app.log", "a") as log_file:
    log_file.write(log_message)

print("Log entry written.")
