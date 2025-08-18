#   Example 2: Myanmar Phone Number Check
# (MPT, TELENOR, Mytel)

import re 

# Test phone numbers
phones = ["09-124562312", "094578524140","09794521452","09694694587"]

# Pattern start with 0-9 and end with 7-9 digits
pattern = r"^09[- ]?\d{7,9}$"

for phone in phones:
    if re.match(pattern, phone):
        print(f"✅ {phone} is a valid Myanmar phone number.")

    else: 
        print(f"❌ {phone} is invalid")
        