import sqlite3

# Create and connect to the database
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# Create sample customer table
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    name TEXT
)
''')

# Create sample product table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
)
''')

# Insert dummy customers (change range for testing conditions)
cursor.executemany("INSERT INTO customers (name) VALUES (?)", [('Customer ' + str(i),) for i in range(1, 651)])

# Insert dummy products
cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", [
    ('Product ' + str(i), i * 10.0) for i in range(1, 51)
])

conn.commit()
conn.close()
