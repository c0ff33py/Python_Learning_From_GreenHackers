# Define a list of letters
letters = ["a", "b", "c", "d", "e", "f"]

# Slice from index 1 to 4 (not including 4)
print(f"letters[1:4]: {letters[1:4]}")  # ['b','c','d']

# Get last 3 elements
print(f"letters[-3:]: {letters[-3:]}")

# Copy entire list
copy = letters[:]
print("Copied list:", copy)
