# List: mutable
my_list = [1, 2, 3]
my_list[0] = 99  # ✅allowed
print(f"List: {my_list}")

# Tuple: immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 99  # ❌ TypeError
print(f"Tuples: {my_tuple}")
