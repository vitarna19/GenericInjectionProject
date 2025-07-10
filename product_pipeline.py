import sqlite3
import json
import sys
import os

def copy_product_data(customer_count):
    if int(customer_count) <= 600:
        print("Customer count not high enough to copy product data.")
        return

    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    os.makedirs("adls", exist_ok=True)
    with open("adls/products.json", "w") as f:
        json.dump(rows, f)

    print(f"Copied {len(rows)} products because customer count was {customer_count}.")
    conn.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        copy_product_data(sys.argv[1])
    else:
        print("No customer count passed to product pipeline.")
