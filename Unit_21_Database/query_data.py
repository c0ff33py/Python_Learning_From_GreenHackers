# query_data.py
import mysql.connector
from config import db_config

try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()

    print("\n Students Data: ")
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

finally:
    if "cursor" in locals():
        cursor.close()
    if "connection" in locals():
        connection.close()
        print("🔌 MySQL connection closed.")