from datetime import datetime


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()

    except FileNotFoundError as e:
        log_msg = f"[{datetime.now()} File not found: {filename}\n ]"
        with open('error.log', 'a') as log:
            log.write(log_msg)

        return "❌ Error: File does not exist."


# Test it
print(read_file("data.txt"))
