# Start with a list of numbers
numbers = [10, 20, 30]
print(numbers)

# Add item to the end with append() method
numbers.append(40)  # [10,20,30,40]
print(numbers)

# Insert 15 at index 1
numbers.insert(1, 15)  # [10,15,20,30,40]
print(numbers)

# Remove value 20
numbers.remove(20)  # [10,15,30,40]
print(numbers)

# Reverse the list
numbers.reverse()  # [40,30,15,10]
print(numbers)

# Sort the list
numbers.sort()  # [10,15,30,40]
print(f"Final numbers: {numbers}")
