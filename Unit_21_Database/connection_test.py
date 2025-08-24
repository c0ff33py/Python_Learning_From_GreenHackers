# connection_test.py

import mysql.connector
from config import db_config

try:
    # Try to connect to Mysql
    connection = mysql.connector.connect(
        host = db_config["host"],
        user = db_config["user"],
        passwd = db_config["password"],
        database = db_config["database"]
    )

    if connection.is_connected():
        print("✅ Connect to MySQL server successfully!.")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔌 MySQL connection closed.")
        
    
        