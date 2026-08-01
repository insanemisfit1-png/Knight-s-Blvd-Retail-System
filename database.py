import sqlite3
class Database:
    def __init__(self):
        self.connection = sqlite3.connect("knight's_blvd.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
size TEXT,
color TEXT,
style TEXT,
price REAL,
stock INTEGER)
""")
        self.connection.commit()

        self.cursor.execute("""INSERT INTO products (name, size, color,  style, price, stock)
VALUES (?, ?, ?, ?, ?, ?)
""",(
    "Black Hoodie",
    "M",
    "Black",
    "Streetwear",
    799.99,
    20)) 

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_name TEXT,
product_name TEXT,
color TEXT,
sale_date TEXT,
total REAL,
quantity INTEGER)
""")
        self.connection.commit()

    def save_sale(self, order):
        self.cursor.execute("""
    INSERT INTO sales(customer_name, product_name, quantity, total, sale_date)
    VALUES (?, ?, ?, ?, ?)
    """, (order.customer.name, order.product.name, order.quantity, order.calculate_total(), order.timestamp))
        self.connection.commit()

    def product_exists(self, name):
        self.cursor.execute("SELECT id FROM products WHERE name = ?", (name,)
    )
        return self.cursor.fetchone() is not None

    def create_tables(self):
        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT  UNIQUE NOT NULL,
    phone TEXT,
    address TEXT)
    """)
        self.connection.commit()

    def save_customer(self, customer):
        self.cursor.execute("""
INSERT INTO customers(name, email, phone, address)
VALUES (?, ?, ?, ?)
""", (customer.name,
    customer.email,
    customer.phone,
    customer.address)
    )
        self.connection.commit()

    def load_customer(self):
        self.cursor.execute("SELECT * FROM customers")
        return self.cursor.fetchall()

    def customer_exists(self, email):
        self.cursor.execute("SELECT id FROM customers WHERE email = ?", (email,)
    )
        return self.cursor.fetchone() is not None

    def delete_customer(self, customer_id):
        self.cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,)
    )
        self.connection.commit()

        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS orders
(id INTEGER PRIMARY KEY AUTOUNCREMENT,
    order_id TEXT,
    customer_name TEXT,
    product_name TEXT,
    quantity INTEGER,
    total REAL,
    status TEXT,
    timestamp TEXT)
    """)
        self.connection.commit()

    def save_product(self, product):
        self.cursor.execute("""
INSERT INTO products (name, size, color, price, stock)
VALUES (?, ?, ?, ?, ?)
""", (
        product.name, 
        product.size,
        product.color, 
        product.price,
        product.stock ))
        self.connection.commit()

    def load_products(self,):
        self.cursor.execute("""
SELECT name, size, color, style, price, stock FROM products""")
        return self.cursor.fetchall()

    def product_exists(self, name):
        self.cursor.execute("SELECT id FROM products WHERE name = ?", (name,)
    )
        return self.cursor.fetchone() is not None

    def get_sales(self):
        self.cursor.execute("SELECT * FROM sales")
        return self.cursor.fetchall()

    def total_products(self):
        self.cursor.execute("SELECT COUNT (*) FROM products")
        return self.cursor.fetchall()[0]

    def total_sales(self):
        self.cursor.execute("""
SELECT SUM(total) FROM sales""")
        return self.cursor.fetchall()[0]

        self.save_customer()
        self.load_customers()
        self.delete_customer()
        self.customer_exists()
        self.connection.commit()

    def update_stock(self, product):
         self.cursor.execute("""UPDATE products
        SET stock = ? WHERE name = ?""", (product.stock, product.name))
         self.connection.commit()

