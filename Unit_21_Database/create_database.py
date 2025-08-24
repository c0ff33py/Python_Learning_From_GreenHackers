# Create database and table
import mysql.connector
from config import db_config


try:
    #Step 1: Connect to Mysql server (no database yet)
    connection = mysql.connector.connect(**db_config) # ** is unpack and connect
    cursor = connection.cursor()

    # Step 2: Create a new database
    cursor.execute("CREATE DATABASE IF NOT EXISTS school_db")
    print("✅ Database 'school_db' created successfully!.")

    # Step 3: Use the new database
    cursor.execute('Use school_db')

    # Step 4: Create a table (students)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            age INT NOT NULL,
            grade VARCHAR(10)
                   )
    """)
    print("✅ Table 'sutdents' created successfully!.")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔌 MySQL connection closed.")    
