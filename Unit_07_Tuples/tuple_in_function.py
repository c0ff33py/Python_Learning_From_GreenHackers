# Function returns multiple values as a tuple
def get_min_max(numbers):
    return min(numbers), max(numbers)


values = [3, 7, 1, 9]
minimum, maximum = get_min_max(values)

print(f"Min: {minimum}")
print(f"Max: {maximum}")
