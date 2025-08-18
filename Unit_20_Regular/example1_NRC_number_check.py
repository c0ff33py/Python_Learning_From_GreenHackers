import re # regex module 

# NRC number
nrc = input("Plese enter NRC : ")

# NRC format
pattern = r"^\d{1,2}/[A-Z]+\(N\)\d{6}$"

# Check NRC
if re.match(pattern, nrc):
    print("✅ Valid NRC format")

else:
    print("❌ Invalid NRC format")
    
