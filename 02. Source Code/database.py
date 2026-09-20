from product import Product
import sqlite3
from pathlib import Path
class Database:
    def __init__(self):
        self.connection = sqlite3.connect("knight's_blvd.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
size TEXT,
price REAL,
color TEXT,
style TEXT,
stock INTEGER)
""")
        self.connection.commit()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_name TEXT,
product_name TEXT,
color TEXT,
style TEXT,
sale_date TEXT,
total REAL,
quantity INTEGER)
""")
        self.connection.commit()

    def save_sale(self, customer_name, product_name, quantity, total):
        self.cursor.execute("""
    INSERT INTO sales(customer_name, product_name, quantity, total, sale_date)
    VALUES (?, ?, ?, ?, datetime('now'))
    """, (customer_name, product_name, quantity, total))
        self.connection.commit()

    def get_sales(self):
            self.cursor.execute("SELECT * FROM sales")
            return self.cursor.fetchall()

    def total_sales(self):
            self.cursor.execute("""
        SELECT SUM(total) FROM sales""")
            return self.cursor.fetchall()[0]
    
            self.save_customer()
            self.load_customers()
            self.delete_customer()
            self.customer_exists()
            self.connection.commit()
    def load_sales(self):
        self.cursor.execute(
        """SELECT customer_name, product_name, quantity, total, sale_date FROM sales
        """
        )
        return self.cursor.fetchall()

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
    address TEXT)""")
        self.connection.commit()

    def save_customer(self, customer):
        self.cursor.execute("""
INSERT INTO customers(name, email, phone, address)
VALUES (?, ?, ?, ?)
""", (customer.name,
    customer.email,
    customer.phone,
    customer.address))
        self.connection.commit()
    def load_customer(self):
        self.cursor.execute("""SELECT name, email, phone, address FROM customers""")
        return self.cursor.fetchall()
    def customer_exists(self, email):
        self.cursor.execute("SELECT id FROM customers WHERE email = ?", (email,) )    
        return self.cursor.fetchone() is not None
    def customer_exists_by_name(self, name):
        self.cursor.execute("SELECT id FROM customers WHERE name = ?", (name,) )    
        return self.cursor.fetchone() is not None
    def delete_customer(self, customer_id):
        self.cursor.execute("DELETE FROM customers WHERE id = ?", (customer_id,))
        self.connection.commit()
        self.cursor.execute("""
CREATE TABLE IF NOT EXISTS orders
(id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id TEXT,
    customer_name TEXT,
    product_name TEXT,
    quantity INTEGER,
    total REAL,
    status TEXT,
    timestamp TEXT)""")
        self.connection.commit()

    def save_product(self, product):
        self.cursor.execute("""
INSERT INTO products (name, size, price, color, style, stock)
VALUES (?, ?, ?, ?, ?, ?)
""", (
        product.name, 
        product.size,
        product.price,
        product.color,
        product.style, 
        product.stock ))
        self.connection.commit()

    def update_product(self, product_id, name, size, price, color, style, stock):
        query = """ UPDATE products
        SET name = ?, size = ?, price = ?, color = ?, style = ?, stock = ? WHERE id = ?"""
        self.cursor.execute(query, (name, size, price, color, style, stock, product_id))
        self.connection.commit()
        return self.cursor.rowcount > 0

    def remove_product(self, product_id):
        query = "DELETE FROM products WHERE id = ?"
        self.cursor.execute(query, (product_id,))
        self.connection.commit()
        return self.cursor.rowcount > 0
    
    def get_product(self, name):
        query = "SELECT * FROM products WHERE name = ?"
        self.cursor.execute(query, (name,))
        return self.cursor.fetchone()
    
    def load_products(self):
        self.cursor.execute("""
SELECT name, size, price, color, style, stock FROM products""")
        rows = self.cursor.fetchall()
        products = []
        for row in rows:
            product = Product(
                row[0],  # name
                row[1],  # size
                row[2],  # price
                row[3],  # color
                row[4],  # style
                row[5]   # stock
            )
            products.append(product)
        return products
    def product_exists(self, name):
        self.cursor.execute("SELECT id FROM products WHERE name = ?", (name,)
    )
        return self.cursor.fetchone() is not None

    def total_products(self):
        self.cursor.execute("SELECT COUNT (*) FROM products")
        return self.cursor.fetchall()[0]

    def update_stock(self, product):
         self.cursor.execute("""UPDATE products
        SET stock = ? WHERE name = ?""", (product.stock, product.name))
         self.connection.commit()

    def close(self):
        self.connection.close() 