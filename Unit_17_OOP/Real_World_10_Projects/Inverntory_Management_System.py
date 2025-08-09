# ==========================================
# Inventory Management System
# ==========================================

# Class Structure
# Thinking Process 
# 1. Product class -> represent of product(name, price, stock)
# 2. Inventory class -> collect products add/update/remove

# Product class

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, new_stock):
        self.stock = new_stock

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})."
    

# Inventory Class
class Inventory:
    def __init__(self):
        self.products = [] # All produccts stored here

    def add_product(self, product):
        self.products.append(product)
        print(f'"{product.name}" added to inventory.')
        
    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print(f'"{product_name}" removed from inventory.')
                return
            print(f'Product"{product_name}" not found in inventory.')
    
    def update_stock(self, product_name, new_stock):
        for product in self.products:
            if product.name == product_name:
                product.update_stock(new_stock)
                print(f" '{product_name}' stock updated to {new_stock}.")
                return
            print(f'Product "{product_name}" not found.')

    def display_inventory(self):
        print("\n Inventory List: ")
        for i, product in enumerate(self.products, start=1):
            print(f"{i}. {product}") 

# Main Program
if __name__ == '__main__':
    inventory = Inventory()

    # Add products 
    inventory.add_product(Product("Laptop", 1200, 5))
    inventory.add_product(Product("Mouse",20, 4))
    inventory.add_product(Product("Keyboard", 45, 30))

    # Show all inventory
    inventory.display_inventory()

    # Updae stock
    inventory.update_stock("Mouse", 40)

    # Remove a product
    inventory.remove_product("Keyboard")

    # Show update inventory
    inventory.display_inventory()


            
        