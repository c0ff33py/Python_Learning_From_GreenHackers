# insert_data.py

import mysql.connector
from config import db_config

try:
    # Step 1: Connect to Mysql server and use the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Step 2: Sql statement to insert data
    sql = "INSERT INTO students(name, age, grade) VALUES(%s, %s, %s)"
    values = [
        ("Alice", 14, "8A"),
        ("Bob", 15, "9B"),
        ("Charlie", 13, "7C")
    ]

    # Step 3: တူညီတဲ့ SQL statement ကို အများကြီး အသုံးပြုချင်ရင် executemany() ကိုသုံး
    cursor.executemany(sql, values)

    # Step 4: DB ကို update မလုပ်မချင်း save မဖြစ်ဘူး -> commit လိုအပ်
    connection.commit()


    print(f"✅ {cursor.rowcount} record(s) inserted successfully.")

except mysql.connector.Error as err:
    print(f"❌ Error: {err}")

finally:
    if "connection" in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("🔌 MySQL connection closed.")
    