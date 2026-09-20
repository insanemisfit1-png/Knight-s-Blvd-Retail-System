import sqlite3

connection = sqlite3.connect("knight's_blvd.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM products")

products = cursor.fetchall()

for product in products:
    print(product)

    
cursor.execute("""
UPDATE products
SET stock = stock - ?
WHERE name = ?
""", (2, "Black Hoodie"))

connection.commit()
connection.close()
