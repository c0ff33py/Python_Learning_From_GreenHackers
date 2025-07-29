# Task: Discount Price Calculator Function
# Function to calculate discount

def calculate_discount(price, percent):
    discount_amount = price * (percent / 100)
    final_price = price - discount_amount
    return final_price


# Example usage
print("Total: ", calculate_discount(100000, 20))
print("Total: ", calculate_discount(1500000, 23))
