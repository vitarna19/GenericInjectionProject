# db_to_adls_pipeline.py

import sqlite3
import json
import os
import subprocess

def copy_customer_data():
    conn = sqlite3.connect('sample.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    count = len(rows)

    print(f"Customer count: {count}")

    if count > 500:
        os.makedirs("adls", exist_ok=True)
        with open("adls/customers.json", "w") as f:
            json.dump(rows, f)
        print("✅ Customer data copied to ADLS (simulated)")

        if count > 600:
            print("📦 Triggering child product pipeline...")
            subprocess.run(["python", "product_pipeline.py", str(count)])

    conn.close()

if __name__ == "__main__":
    copy_customer_data()
