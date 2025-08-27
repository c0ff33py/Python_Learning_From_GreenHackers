#   Step 1: Database and Tables Design
#   customers (customer info)
#   products (product info)
#   orders (order info)

import mysql.connector

# Connect to MySQL (no db selected yet)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password here"
)
cursor = db.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce_db")
print("✅ Database created.")

# Reconnect to use ecommerce_db
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password here",
    database="ecommerce_db"
)
cursor = db.cursor()

# Create Customers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")

# Create Products Table (⚡ missing in your code)
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    stock INT
)
""")

# Create Orders table (fixed FOREIGN KEY references)
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
)
""")

print("✅ Tables created successfully.")

# Step 2: Insert Sample Data
# Insert customers
cursor.executemany(
    "INSERT INTO customers (name, email) VALUES (%s, %s)",
    [
        ("Alice", "alice@dd.com"),
        ("Bob", "bob@cc.com")
    ]
)
db.commit()

# Insert products
cursor.executemany(
    "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
    [
        ("Laptop", 1200.00, 10),
        ("Phone", 600.00, 24),
        ("Headphone", 50.00, 50)
    ]
)
db.commit()

print("✅ Customers & Products inserted.")

# Step 3: Place an order
cursor.execute(
    "INSERT INTO orders (customer_id, product_id, quantity) VALUES (%s, %s, %s)",
    (1, 2, 2)  # Alice (id=1), Phone (id=2), qty=2
)
db.commit()
print("✅ Order placed!")

# Reduce stock
cursor.execute("UPDATE products SET stock = stock - %s WHERE id = %s", (2, 2))
db.commit()
print("✅ Product stock updated!")

# Step 4: View Orders with JOIN
cursor.execute("""
SELECT customers.name AS customer_name, 
       products.name AS product_name, 
       orders.quantity
FROM orders
JOIN customers ON orders.customer_id = customers.id
JOIN products ON orders.product_id = products.id
""")
result = cursor.fetchall()

print("📦 Order History")
for row in result:
    print(row)

# Step 5: Update and Cancel Orders
# Update order quantity
cursor.execute("UPDATE orders SET quantity = %s WHERE id = %s", (3, 1))
db.commit()
print("✏️ Order updated!")

# Cancel order (delete)
cursor.execute("DELETE FROM orders WHERE id = %s", (1,))
db.commit()
print("❌ Order cancelled!")
