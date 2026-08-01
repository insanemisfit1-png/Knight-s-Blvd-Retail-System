print("Welcome to project Knight.")
print("Knight AI is under construction.")
print("Built by Nkosinathi.")
print("Brick by brick.")

from product import Product
from customer import Customer
from order import Order
from receipt import Receipt
from inventory import Inventory
from store import Store
from database import Database


db = Database()
db.create_tables()
hoodie  =   Product(
    "Black Hoodie",
    "Medium",
    799.99,
    "Black",
    "Streetwear",
    2)
hoodie.show_details()
customer1 = Customer("Bhlomingtn", "bhlomingtn@email.com", "0710345678", "Johannesburg")
order1 = Order("0R001", customer1, hoodie, 2)
order1.display_order()

tshirt  =   Product(
    "Black T-Shirt",
    "Medium",
    299.99,
    "Black",
    "Streetwear",
    5)
tshirt.show_details()
customer2 = Customer("Bloom Pot", "bloom@email.com", "0712355678", "Johannesburg")
order2 = Order("0R002", customer2, tshirt, 2)
order2.display_order()

cargo_pants   =     Product(
    "Black Cargo Pants",
    "Medium",
    799.99,
    "Black",
    "Streetwear",
    6)
cargo_pants.show_details()
customer3 = Customer("Bhlom Doe", "Bhlom@email.com", "0712345778", "Johannesburg")
order3 = Order("0R003", customer3, cargo_pants, 2)
order3.display_order()

denim_jeans =   Product(
    "Black Denim Jeans",
    "Medium",
    799.99,
    "Black",
    "Streetwear",
    15)
denim_jeans.show_details()
customer4 = Customer("John Raven", "johnny@email.com", "0702349678", "Johannesburg")
order4 = Order("0R004", customer4, denim_jeans, 2)
order4.display_order()

shirt   =   Product(
    "Black Shirt",
    "Medium",
    399.99,
    "Black",
    "Streetwear",
    12)
shirt.show_details()
customer5 = Customer("Jane Smith", "jane@email.com", "0612345678", "Johannesburg")
order5 = Order("0R005", customer5, shirt, 2)
order5.display_order()

sweater =  Product(
    "Black Sweater",
    "Medium",
    599.99,
    "Black",
    "Streetwear",
    3)
sweater.show_details()
customer6 = Customer("Jane Doe", "jane@email.com", "0812345678", "Johannesburg")
order6 = Order("0R006", customer6, sweater, 2)
order6.display_order()

windbreaker =   Product(
    "Black Windbreaker",
    "Medium",
    799.99,
    "Black",
    "Streetwear",
    5)
windbreaker.show_details()
customer7 = Customer("Bonnie Doe", "bonnie@email.com", "0742345678", "Johannesburg")
order7 = Order("0R007", customer7, windbreaker, 2)
order7.display_order()

bomber_jacket   =   Product(
    "Black Bomber Jacket",
    "Medium",
    999.99,
    "Black",
    "Streetwear",
    2)
bomber_jacket.show_details()
customer8 = Customer("Late Blvd", "lateblvd@email.com", "0713345678", "Johannesburg")
order8 = Order("0R008", customer8, bomber_jacket, 2)
order8.display_order()

baseball_cap    =  Product(
    "Black Baseball Cap",
    "Medium",
    599.99,
    "Black",
    "Streetwear",
    4)
baseball_cap.show_details()
customer9 = Customer("Nkosi", "nkosi@email.com", "0712645678", "Johannesburg")
order9 = Order("0R009", customer9, baseball_cap, 2)
order9.display_order()

bucket_hat  =  Product(
    "Black Bucket Hat",
    "Medium",
    599.99,
    "Black",
    "Streetwear",
    2)
bucket_hat.show_details()
customer10 = Customer("Revenge", "revenge@email.com", "0712345674", "Johannesburg")
order10 = Order("0R0010", customer10, bucket_hat, 2)
order10.display_order()

beanie  =   Product(
    "Black Beanie",
    "Medium",
    599.99,
    "Black",
    "Streetwear",
    2)
beanie.show_details()
customer11 = Customer("Alice Johnson", "alice@email.com", "0712345678", "Johannesburg")
order11 = Order("0R0011", customer11, beanie, 2)
order11.display_order()

panel_cap   =   Product(
    "Black Panel Cap",
    "Medium",
    799.99,
    "Black",
    "Streetwear",
    6)
panel_cap.show_details()
customer12 = Customer("Omar ", "omar@email.com", "0712345678", "Johannesburg")
order12 = Order("0R0012", customer12, panel_cap, 2)
order12.display_order()

wide_leg_pants  =   Product(
    "Black Wide Leg Pants",
    "Medium",
    799.99,
    "Black",
    "Streetwear",
    1)
wide_leg_pants.show_details()
customer13 = Customer("Joe Doe", "joe@email.com", "0712345623", "Johannesburg")
order13 = Order("0R0013", customer13, wide_leg_pants, 2)
order13.display_order()

track_pants =   Product(
    "Black Track Pants",
    "Medium",
    799.99,
    "Black",
    "Streetwear",
    2)
track_pants.show_details()
customer14 = Customer("Hendricks", "hendricks@email.com", "0712885678", "Johannesburg")
order14 = Order("0R0014", customer14, track_pants, 2)
order14.display_order()

tank_top    =   Product(
    "Black tank_top",
    "Medium",
    299.99,
    "Black",
    "Streetwear",
    1)
tank_top.show_details()
customer15 = Customer("Sarah Wilson", "sarah@email.com", "0712345978", "Johannesburg")
order15 = Order("0R0015", customer15, tank_top, 2)
order15.display_order()

db.update_stock(order1.product)
db.update_stock(order2.product)
db.update_stock(order3.product)
db.update_stock(order4.product)
db.update_stock(order5.product)
db.update_stock(order6.product)
db.update_stock(order7.product)
db.update_stock(order8.product)
db.update_stock(order9.product)
db.update_stock(order10.product)
db.update_stock(order11.product)
db.update_stock(order12.product)
db.update_stock(order1.product)
db.update_stock(order14.product)
db.update_stock(order15.product)

if not db.product_exists(hoodie.name):    db.save_product(hoodie)
if not db.product_exists(tshirt.name):    db.save_product(tshirt)
if not db.product_exists(cargo_pants.name):    db.save_product(cargo_pants)
if not db.product_exists(denim_jeans.name):    db.save_product(denim_jeans)
if not db.product_exists(shirt.name):    db.save_product(shirt)
if not db.product_exists(sweater.name):    db.save_product(sweater)
if not db.product_exists(windbreaker.name):    db.save_product(windbreaker)
if not db.product_exists(bomber_jacket.name):    db.save_product(bomber_jacket)
if not db.product_exists(baseball_cap.name):    db.save_product(baseball_cap)
if not db.product_exists(bucket_hat.name):    db.save_product(bucket_hat)
if not db.product_exists(beanie.name):    db.save_product(beanie)
if not db.product_exists(panel_cap.name):    db.save_product(panel_cap)
if not db.product_exists(wide_leg_pants.name):    db.save_product(wide_leg_pants)
if not db.product_exists(track_pants.name):    db.save_product(track_pants)
if not db.product_exists(tank_top.name):    db.save_product(tank_top)

if not db.customer_exists(customer1.email):
    db.save_customer(customer1)
if not db.customer_exists(customer2.email):
    db.save_customer(customer2)
if not db.customer_exists(customer3.email):
    db.save_customer(customer3)
if not db.customer_exists(customer4.email):
    db.save_customer(customer4)
if not db.customer_exists(customer5.email):
    db.save_customer(customer5)
if not db.customer_exists(customer6.email):
        db.save_customer(customer6)
if not db.customer_exists(customer7.email):
    db.save_customer(customer7)
if not db.customer_exists(customer8.email):
    db.save_customer(customer8)
if not db.customer_exists(customer9.email):
    db.save_customer(customer9)
if not db.customer_exists(customer10.email):
    db.save_customer(customer10)
if not db.customer_exists(customer11.email):
    db.save_customer(customer11)
if not db.customer_exists(customer12.email):
    db.save_customer(customer12)
if not db.customer_exists(customer14.email):
    db.save_customer(customer14)
if not db.customer_exists(customer15.email):
    db.save_customer(customer15)
orders = [order1, order2, order3, order4, order5, order6, order7, order8, order9, order10, order11, order12, order13, order14, order15]
for order in orders:
    if order.checkout():
        print(f"Order {order.order_id} for {order.customer.name} has been successfully checked out.")
order.checkout()
db.save_sale(order)

products = db.load_products()
for product in products:
    print(product)

def close(self):
    self.connection.close()
    db.close()

def main():
    while True:
        print("\n=====  Knight's Blvd   =====")
        print("1. View Products")
        print("2. Add Products")
        print("3. Search Product")
        print("4. Add Customer")
        print("5. Place Order")
        print("6. View Sales")
        print("7. Exit")
        choice  =   input("Choose an option:    ")

        if choice == "7":
            print("Thank you for using Knight's Blvd.")
            db.close()
            break
        
        if choice == "1" :   
            print("Viewing products...")
        
        if choice == "2":
            print("Adding products...")
        
        if choice == "3":
            print("Searching products...")
        
        if choice == "4":
            print("Adding customer...")
        
        if choice == "5":
            print("Placing order...")
        
        if choice == "6":
            print("Viewing sales...")

        if choice == "7":
            print("Thank you for using Knight's Blvd.")
            db.close()
            break

        if __name__ == "__main__":
            main()


receipt = Receipt(order1)
receipt.generate_receipt()














