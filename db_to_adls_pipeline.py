import sqlite3
import json
import os

def copy_customer_data():
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    data = cursor.fetchall()
    count = len(data)

    if count > 500:
        os.makedirs("adls", exist_ok=True)
        with open("adls/customers.json", "w") as f:
            json.dump(data, f)
        print("Customer data copied")

        if count > 600:
            copy_product_data(count)

    conn.close()

def copy_product_data(customer_count):
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()

    with open("adls/products.json", "w") as f:
        json.dump(data, f)

    print(f"Product data copied because customer count was {customer_count}")
