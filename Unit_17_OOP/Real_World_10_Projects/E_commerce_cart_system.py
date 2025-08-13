# E-Commercce Cart System

class Product:
    def __init__(self, name, price):
        self.name = name # Product name
        self.price = price # Product price

class Cart:
    def __init__(self):
        self.items = [] # List to store products in the cart

    def add_to_cart(self, product):
        """ADD a product to the cart"""
        self.items.append(product)
        print(f"'✅{product.name}' added to cart.")
        
    def remove_from_cart(self, product_name):
        """Remove a product by name"""
        for item in self.items:
            if item.name.lower() == product_name.lower():
                self.items.remove(item)
                print(f" '{item.name}' removed from cart.")
                return
        print("❌ Product not found in cart.")

    def show_cart(self):
        """Display all products in the cart"""
        if not self.items:
            print('🗑️ Your cart is empty.')
            return
        print("\n🛍️ Your Cart: ")
        for idx, item in enumerate(self.items, start=1):
            print(f"{idx}. {item.name}- ${item.price:.2f}")
            
    def checkout(self):
        """Calculate and display total bill"""
        if not self.items:
            print("Your cat is empty. Cannot checkout.")
            return
        total = sum(item.price for item in self.items)
        print("\n Checkout Summary: ")
        for item in self.items:
            print(f"- {item.name} - ${item.price:.2f}")
        print(f"\n Total: ${total:.2f}")
        self.items.clear()
        print("✅ Purchase completed! Thank you, see you soon.")


class EComerceApp:
    def __init__(self):
        self.products = [
            Product("Laptop", 2000),
            Product("Phone", 855),
            Product("Headphones", 150),
            Product("Keyboard",20)
        ]
        self.cart = Cart()
            
    def show_products(self):
        """Display available products"""
        print("\n 📦Available Products: ")
        for idx, product in enumerate(self.products, start=1):
            print(f"{idx}. {product.name} - ${product.price:.2f}")

    def menu(self):
        """Main Menu"""
        while True:
            print('\n====🛒 E-Commerce Menu======')
            print('1. View Products')
            print('2. Add to Cart')
            print('3. Remove from Cart')
            print('4. View Cart')
            print('5. Checkout')
            print('6. Exit')

            choose = input("Choose an option: ")
            if choose == "1":
                self.show_products()
            elif choose =="2":
                self.show_products()
                prod_num = input("Enter product number to add: ")
                if prod_num.isdigit() and 1 <= int(prod_num) <=len(self.products):
                    self.cart.add_to_cart(self.products[int(prod_num) - 1])
                else:
                    print("❌ Invalid selection.")

            elif choose == "3":
                name = input("Enter product name to remove: ")
                self.cart.remove_from_cart(name)

            elif choose == "4":
                self.cart.show_cart()

            elif choose =="5":
                self.cart.checkout()

            elif choose == "6":
                print("Goodbye!")
                break
            else:
                print('❌ Invalid opiton.')
#==== Run the App===
app = EComerceApp()
app.menu()
                
            
            
            
            