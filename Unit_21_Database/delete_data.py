# delete_data.py
import mysql.connector
from config import db_config

try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    sql = "DELETE FROM students WHERE name = %s"
    value = ("Charlie",)

    cursor.execute(sql, value)
    connection.commit()

    print(f"✅ {cursor.rowcount} record(s) deleted successfully!")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")
finally:
    if "cursor" in locals():
        cursor.close()
    if "connection" in locals() and connection.is_connected():
        connection.close()
        print("🔌 MySQL connection closed.")
