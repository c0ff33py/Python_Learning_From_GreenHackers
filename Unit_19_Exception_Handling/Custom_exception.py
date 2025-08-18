# Exercise 4 - Custom exception

# Step 1: Create a custom exception

class UnderAgeError(Exception):
    """Raised when user is under 18 years old"""
    pass
try:
    # Step 2: Get age from user
    age = int(input("Enter your age: "))

    # Step 3: check age condition
    if age < 18:
        # Raise custom exception
        raise UnderAgeError("❌ You must be at least 18 years old to continue.")
    # if no exception raised
    print("✅ Access Granted! Welcome.")


except UnderAgeError as e:
    # Step 4: Handle custom exception
    print(e)

except ValueError:
    # Step 5: Handle invalid input
    print("❌ Please enter a valid number for age.")

finally:
    #Always executed
    print("👉 Age check complete.")
    
    
    
    