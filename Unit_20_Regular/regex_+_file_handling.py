import re

def analyze_logs(file_path):
    #Regex patterns

    ip_pattern = r"\b\d{1,3}(?:\.\d{1,3}){3}\b" # IPv4 address
    date_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}" #Date-time
    error_pattern = r"ERROR|WARN|CRITICAL" # Error keywords

    with open(file_path, "r") as file:
        logs = file.readlines()

    print("\n📊 Log Analysis Report:")
    for line in logs:
        ip = re.search(ip_pattern, line)
        date = re.search(date_pattern, line)
        error = re.search(error_pattern, line)

        if error: #Only show error lines
            print(f"{date.group() if date else 'Unknown time'} | "
                  f"IP: {ip.group() if ip else 'N/A'} | "
                  f"Error: {error.group()} | "
                  f"Log: {line.strip()}")  
# ----------------------------
# Example Usage
# ----------------------------
# Sample log file content (save as 'server.log'):
"""
2025-08-17 15:12:43 192.168.1.10 INFO User login success
2025-08-17 15:13:10 192.168.1.15 ERROR Database connection failed
2025-08-17 15:14:22 10.0.0.5 WARN Low disk space
2025-08-17 15:15:01 192.168.1.20 CRITICAL Kernel panic
"""

analyze_logs("server.log")   