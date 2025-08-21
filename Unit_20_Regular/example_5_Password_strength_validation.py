import re

def check_password_strength(password):
    # Regex rules
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    if re.match(pattern, password):
        return "✅ Strong Password"
    else:
        return "❌ Weak Password"
    
# Test passwords
print(check_password_strength("Python123")) # weak(no special char)
print(check_password_strength("Python@123")) #Strong
print(check_password_strength("pass@1")) # weak (too short)
print(check_password_strength("aeiOu$we@Live123")) # strong