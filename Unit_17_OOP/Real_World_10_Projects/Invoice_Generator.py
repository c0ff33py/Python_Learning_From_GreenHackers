# Project 9: Invoice Generator

class InvoiceGenerator:
    def __init__(self):
        self.items = [] # Store all purchased items

    def add_item(self, name, qty, price):
        """Add an item to the invoice"""
        self.items.append({
            "name": name,
            "qty": qty,
            "price": price
        })
        print(f"✅ '{name} added to invoice.")

    def calculate_totals(self, tax_rate=0.05, discount =0):
        """Calculate subtotal, tax, discount and grand total"""
        subtotal = sum(item["qty"] * item["price"] for item in self.items)
        tax = subtotal * tax_rate
        grand_total = subtotal + tax - discount
        return subtotal, tax, discount, grand_total
    
    def generate_invoice(self):
        """Display the invoice details"""
        print('\n🗒️ Invoice: ')
        print('-' * 40)
        for item in self.items:
            print(f'{item['name']} (x{item['qty']}) - ${item['price']:.2f} each')
        subtotal, tax, discount, grand_toal = self.calculate_totals()
        print('-' * 40)
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Discount: ${discount:.2f}")
        print(f'Grand Total: ${grand_toal:.2f}')

    def save_invoice(self, filename="invoice.txt"):
        """Save the invoice as a text file"""
        with open(filename, "w") as f:
            f.write("🗒️ Invoice\n")
            f.write("-"*40 + "\n")
            for item in self.items:
                f.write(f"{item['name']} (x{item['qty']}) - ${item['price']:.2f} each\n")
            subtotal, tax, discount, grand_total = self.calculate_totals()    
            f.write("-" * 40 + "\n")
            f.write(f"Subtotal: ${subtotal:.2f}\n")
            f.write(f"Tax: ${tax:.2f}\n")
            f.write(f"Discount: ${discount:.2f}\n")
            f.write(f"Grand Total: ${grand_total:.2f}\n")
        print(f"💾 Invoice saved as {filename}")
        
# --------Example Usage---------
invoice = InvoiceGenerator()
invoice.add_item("Laptop", 2, 999)
invoice.add_item("Macbook", 5, 1999)
invoice.generate_invoice()
invoice.save_invoice()
            
            
        
        