# Basic patterns

import re

# Example 1: Basic Patterns
text1 = "Order 123 will be delivered on 20025-08-21"
digits = re.findall(r"\d+", text1)
print("Digits found:", digits)

# Example 2: Validate simple email format
text2 = "My email is test@exa.com"
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
match = re.search(email_pattern, text2)
if match:
    print("Valid email found:", match.group())

# Example 3: Extract Myanmar phone number
text3 = "Customer phone: 09123456789"
phone_pattern = r"09\d{7,9}" # Starts with 09 and has 9-11 digits total
match = re.search(phone_pattern, text3)
if match:
    print("Myanmar phone number:", match.group())
        