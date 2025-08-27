import mysql.connector

#   Step1: Connect to MySQL
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "your password here"
)

cursor = db.cursor()

#   Step 2: Database create
cursor.execute("CREATE DATABASE IF NOT EXISTS employee_db")
print("✅ Database created!")

#   Step 3: Database connect
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "your password here",
    database = "employee_db"
)
cursor = db.cursor()

#   Step 4: Table create
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10, 2)       
)
""")
print("✅ Table created.")

#   Step 5: Insert data
sql = "INSERT INTO employees(name, department, salary) VALUES (%s, %s, %s)"
values = [
    ("Alice", "IT", 75000.00),
    ("Bob", "HR", 50000.00),
    ("Charlie", "Finance", 65000.00)
]
cursor.executemany(sql, values)
db.commit()
print("✅ Data inserted!")

#   Step 6: Select data
cursor.execute("SELECT * FROM employees WHERE department ='IT'")
result = cursor.fetchall()
print("IT Department Employees:")
for row in result:
    print(row)

#   Step 7: Update + Delete
cursor.execute("UPDATE employees SET salary = %s WHERE name =%s", (50000.00, "Bob"))
db.commit()
print(" Bob's salary updated!")

cursor.execute("DELETE FROM employees WHERE name = %s", ("Charlie",))
db.commit()
print("✅ Charlie deleted!")

