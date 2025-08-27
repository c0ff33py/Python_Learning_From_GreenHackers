import mysql.connector

# Connect to DB

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "pythonmac",
    database = "password here"
)

cursor = db.cursor()

# Insert new sample order for testing
cursor.execute("INSERT INTO orders (customer_id, product_id, quantity) VALUES (%s, %s, %s)",
               (2, 1, 1)) # Bob buys 1 laptop
db.commit()

print("✅ New Order Inserted!.")

#View order History with total price
cursor.execute(""" 
SELECT customers.name,
        products.name,
        orders.quantity,
        products.price,
        (orders.quantity * products.price) As total_price FROM orders
        JOIN customers ON orders.customer_id = customers.id
        JOIN products ON orders.product_id = products.id
""")

result = cursor.fetchall()

print("\n Order History with Total Price:")
print("Customer | Product | Quantity| Total|")
for row in result:
    print(row)