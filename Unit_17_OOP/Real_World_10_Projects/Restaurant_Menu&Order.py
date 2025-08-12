# ----------------------------------
# Restaurant Menu & Ordering System
# ----------------------------------
# Author: c0ff33py

class MenuItem:
    """Represents one menu item with name and price"""
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Restaurant:
    """Handles menu display, order taking, and billing."""
    def __init__(self):
        # Step 1 : Create a menu list
        self.menu = [
            MenuItem("Burger", 5.50),
            MenuItem("Pizza", 8.99),
            MenuItem("Pasta", 7.25),
            MenuItem("Coffee", 2.50),
            MenuItem("Tea", 1.75)
        ]
        self.orders = [] # Store ordered items

    def show_menu(self):
        """Display the menu items"""
        print('\n Restaurant Menu: ')
        for idx, item in enumerate(self.menu, start=1):
            print(f'{idx}. {item.name} - ${item.price:.2f}')

    def take_order(self):
        """Ask the customer to order by menu number"""
        while True:
            self.show_menu()
            choice = input('\n Enter item number to order (or "q" to finish): ')
            if choice.lower() == 'q':
                break # Stop ordering

            if choice.isdigit() and 1 <= int(choice) <= len(self.menu):
                selected_item = self.menu[int(choice) - 1]
                self.orders.append(selected_item)
                print(f'{selected_item.name} added to your order.')
            else:
                print('Invalid choice, Please try again.')

    def calculate_bill(self):
        """Calculate the total price of all orders"""
        total = sum(item.price for item in self.orders) 
        print('\n Your Order Summary: ')
        for item in self.orders:
            print(f'- {item.name} - ${item.price:.2f}')
        print(f"\n Total Bill: ${total:.2f}")
# ----------------------
# Main Program
# ----------------------
restaurant = Restaurant()
restaurant.take_order()
restaurant.calculate_bill()           
                       
                
                            
        