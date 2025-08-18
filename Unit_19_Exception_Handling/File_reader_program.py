# Exercise 2 - File Reader with Exception Handling

try:
    # User enters file name
    file_name = input("Enter file name to read: ")
    
    # Try opening the file in read mode
    with open(file_name, "r") as f:
        content = f.read()
        print("\n📄 File Content: ")
        print(content)

except FileNotFoundError:
    # Handle case where file does not exist
    print("❌ Error: File not found. Please check the filename again.")

except PermissionError:
    # Handle case where user has no permission to read file
    print("❌ Error: You don't have permission to read this file.")

finally:
    # Always run this block
    print("👉 File reading attempt finished.")
    
    
    
        
        