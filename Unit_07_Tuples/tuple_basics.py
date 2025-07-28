# Creating a tuple
fruits = ("apple", "banana", "orange")

# Accessing elements
print("First fruit: ", fruits[0])  # output :apple
print("Last fruit: ", fruits[-1])  # output: orange

# Length of the tuple
print(f"Total fruits: {len(fruits)}")  # output: 3

# Tuples are immutable, so this will cause an error:
# fruits[1] = "cherry" ❎ TypeError
