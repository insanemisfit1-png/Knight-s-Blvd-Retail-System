print("THIS IS THE RUNNING MAIN FILE")
from product import Product
from customer import Customer
from order import Order
from receipt import Receipt
from inventory import Inventory
from store import Store
from database import Database

db = Database()
db.create_tables()

inventory = Inventory()

products = db.load_products()
for product in products:
    inventory.add_product(product)

for row in db.load_products():
    product = Product
    inventory.add_product(product)
store = Store("Knight's Blvd", inventory, db)

def main():
    while True:
        print("\n=====  Knight's Blvd   =====")
        print("1. View Products")
        print("2. Add Products")
        print("3. Search Product")
        print("4. Add Customer")
        print("5. View Customers")
        print("6. Place Order")
        print("7. Sales History")
        print("8. Update Product")
        print("9. Delete Product")
        print("10. Exit")
        choice = input("Choose an option:    ")
        print("You chose option:", choice)

        if choice == "1" :   
           
           store.view_products()

        elif choice == "2":

            print("=====    Add Products    =====")
            name = input("Product Name: ")
            size = input("Size: ")
            try:
                price = float(input("Price: "))
            except ValueError:
                print("Invalid price. Please enter a number.")
                continue
            color = input("Color: ")
            style = input("Style: ")
            stock = int(input(" Stock quantity: "))
            product = Product(name, size, price, color, style, stock)
            store.add_product(product)
            if not db.product_exists(product.name):
                    db.save_product(product)
                    print(f"Product {product.name} added successfully.")
            else:
                    print(f"Product {product.name} already exists in the database.")

        elif choice == "3":
            print("Searching products...")
            product_name = input("Enter product name to search: ")
            product = inventory.search_by_name(product_name)

            if product:
                print(f"Product found: {product.name}, Size: {product.size}, Price: R{product.price:.2f}")
                print(f"Color: {product.color}, Style: {product.style}, Stock: {product.stock}")
            else:
                print("Product not found.")

        elif choice == "4":
            print("Adding customer...")
            name = input("Customer Name: ")
            email = input("Customer Email: ")
            phone = input("Customer Phone: ")
            address = input("Customer Address: ")
            customer = Customer(name, email, phone, address)
            if not db.customer_exists(customer.email):
                db.save_customer(customer)
                print(f"Customer {customer.name} added successfully.")
            else:
                print(f"Customer {customer.name} already exists in the database.")

        elif choice == "5":
            print("Viewing customers...")
            customers = db.load_customer()
            if not customers:
                print("No customers found.")
            else:
                for customer in customers:
                    print(f"Name: {customer[0]}, Email: {customer[1]}, Phone: {customer[2]}, Address: {customer[3]}")
                    
        elif choice == "6":
            print("Placing order...")
            customer_name = input("Customer" \
            " name:   ")
            product_name = input("Product " \
            "name: ")
            try:
                quantity = int(input("Quantity:"))
            except ValueError:
                print("Invalid quantity. Please enter a number.")
                continue

            store.sell_product(customer_name, product_name, quantity)

        elif choice == "7":
            print(" Sales History:")
            sales = db.load_sales()
            if not sales:
                print("No sales found.")
            else:
                for sale in sales:
                    print( 
                        f"Customer: {sale[0]}", 
                        f"Product: {sale[1]}", 
                        f"Quantity: {sale[2]}", 
                        f"Total: R{sale[3]:.2f}", 
                        f"Date: {sale[4]}")

        elif choice == "8":
            product_name = input("Enter the product name to update: ")
            product = db.get_product(product_name)
            if product:
                print("\nProduct found.")
                print("Leave a field blank to keep the current value. \n")

                name = input(f"Name [{product[1]}]: ") or product[1]
                size = input(f"Size [{product[2]}]: ") or product[2]
                price = input(f"Price [{product[3]}]: ") or product[3]
                color = input(f"Color [{product[4]}]: ") or product[4]
                style = input(f"Style [{product[5]}]: ") or product[5]
                stock = input(f"Stock [{product[6]}]: ") or product[6]

                db.update_product(product[0], name, size, price, color, style, stock)
                print("Product updated successfully.")
            else:
                print("Product not found.")

        elif choice == "9":
            product_name = input("Enter the product name to delete: ")
            product = db.get_product(product_name)
            if product:
                print(f"\nProduct found: {product[1]}")
                confirm = input(f"Are you sure you want to remove this {product[1]}? (y/n): ").lower()

                if confirm.lower() == 'y':
                    removed = db.remove_product(product[0])

                if removed:    
                    print("\nProduct deleted successfully.")
                else:
                    print("\nFailed to delete product.")
            else:
                print("\nProduct not found.")

        elif choice == "10":
            print("Thank you for using Knight's Blvd.")
            break
            
    db.close()
                
if __name__ == "__main__":
    print("=====   MAIN STARTED   =====")
    print(__file__)
    main()



