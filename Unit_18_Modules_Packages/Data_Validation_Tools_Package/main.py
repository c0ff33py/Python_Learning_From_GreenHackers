# main.py
from data_validator import is_integer, is_string, in_range, positive

# Example dataset
data = {
    "name": "Alice",
    "age": 25,
    "height": 1.68,
    "balance": -100
}

# Validations
print("Is name a string?", is_string(data["name"]))
print("Is age an integer?", is_integer(data["age"]))
print("Is height in range (1.5 to 2.0)?", in_range(data["height"], 1.5, 2.0))
print("Is balance positive?", positive(data["balance"]))



