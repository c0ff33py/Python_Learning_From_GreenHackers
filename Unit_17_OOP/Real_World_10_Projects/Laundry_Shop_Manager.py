# Project 2: Laundry Shop Manager
""" GOAL
Build a System for a Lundry shop where:
-   Customer can drop off clothes
-   Each laundry item has a type and wash type
-   Track washing status(Pending -> In Progress -> Done)
-   Calculate total cost
-   Allow multiple customers

"""
"""Design Structure:
-   LaundryItem_class = Represents each item(type, wash type, price, status)
-   Customer class = Holds customer name and item list
"""

# class representing a laundry item


class LaundryItem:
    def __init__(self, item_type, wash_type, price):
        self.item_type = item_type  # e.g shirt, pants
        self.wash_type = wash_type  # e.g normal, dry clean
        self.price = price  # price per item
        self.status = "Pending"  # default status

# Update washing status
    def update_status(self, new_status):
        if new_status in ["Pending", "In Progress", "Done"]:
            self.status = new_status
        else:
            print("❌ Invalid status.")

    # Represent item as string
    def __str__(self):
        return f"{self.item_type} ({self.wash_type}) - {self.price} MMK [{self.status}]"

# Class representing a customer


class Customer:
    def __init__(self, name):
        self.name = name
        self.items = []  # List to store LaundryItem objects

    # Add laundry item to customer
    def add_item(self, item):
        self.items.append(item)

    # Get total cost
    def total_cost(self):
        return sum(item.price for item in self.items)

    # Display all items
    def show_items(self):
        print(f'\n Laundry for {self.name}: ')
        for i, item in enumerate(self.items, 1):
            print(f'{i}. {item}')
        print(f"Total : {self.total_cost()} MMK")

# ---------------------------
# Simulate the system
# ---------------------------


# Create customer
customer1 = Customer("c0ff33py")

# Add items
item1 = LaundryItem("Shirt", "Normal Wash", 1000)
item2 = LaundryItem("Pants", "Dry Clean", 2000)

customer1.add_item(item1)
customer1.add_item(item2)

# Show initial
customer1.show_items()

# Update status of an item
item1.update_status("In Progress")
item2.update_status("Done")

# Show updated
customer1.show_items()
