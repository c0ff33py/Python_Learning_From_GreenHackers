import json
import os

filename = "products.json"

# Load existing product list
if os.path.exists(filename):
    with open(filename, "r") as f:
        inventory = json.load(f)

else:
    inventory = []

# Add a product
product = {
    "id": len(inventory) + 1,
    "name": input("Product name: "),
    "price": float(input("Price: "))
}
inventory.append(product)

# Save updated inventory
with open(filename, "w") as f:
    json.dump(inventory, f, indent=2)

print("Product added.")
