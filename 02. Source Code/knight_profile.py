
product = "Black Hoodie"
size = "Medium"
price = "799.99"
color = "Black"
style = "Streetwear"
age = 22
name = "Bhlomingtn"


name = input("What's your name?")
print("Welcome,", name)

product = input("what product are you looking for?")
size = input("what size do you need?") 


budget = 600
if budget >= 800:
      print("Premium Hoodie")
else:
      print("Standard Hoodie") 


      budget = 1200

      if budget >= 1200:
        print("Luxury Collection")
      elif budget>= 800:
          print("Premium Collection")
      else:
          print("Essential Collection")

        




budget = int( input("what's your budget?"))
print("Welcome,", name)

if budget>= 1200:
        print("We recommennd our Luxury Collection.")
elif budget>= 800:
          print("We recommend our Premium Collection.")
else:
          print("We recommend our Essential Collection.")


# Abstract budget class and a concrete implementation
from abc import ABC, abstractmethod


class budget(ABC):
  """Abstract budget interface."""

  @abstractmethod
  def set_budget(self, amount: float):
    pass

  @abstractmethod
  def get_budget(self) -> float:
    pass

  @abstractmethod
  def recommend_collection(self) -> str:
    pass

  @abstractmethod
  def apply_discount(self, price: float) -> float:
    pass


class BudgetImpl(budget):
  """Concrete implementation of budget logic."""

  def __init__(self, amount: float = 0.0):
    self._budget = float(amount)

  def set_budget(self, amount: float):
    self._budget = float(amount)

  def get_budget(self) -> float:
    return self._budget

  def recommend_collection(self) -> str:
    if self._budget >= 1200:
      return "Luxury Collection"
    if self._budget >= 800:
      return "Premium Collection"
    return "Essential Collection"

  def apply_discount(self, price: float) -> float:
    """Apply a simple discount based on budget tiers.

    - Luxury: 20% off
    - Premium: 10% off
    - Essential: 0% off
    """
    if price is None:
      return 0.0
    p = float(price)
    if self._budget >= 1200:
      return round(p * 0.80, 2)
    if self._budget >= 800:
      return round(p * 0.90, 2)
    return round(p, 2)


# Example usage (non-intrusive): create an instance if budget variable exists
try:
  _b = BudgetImpl(budget)
except Exception:
  _b = BudgetImpl(0)





product = product[0]  # Assuming the first product is the one to sell
product = self.inventory.search_by_name(product_name)
print("    store received:", repr(product_name))  # Debugging line     

if item.name.lower() == product_name.lower():
                product = item
                break


               print( 
                    f"Customer: {sale[0]}", 
                    f"Product: {sale[1]}", 
                    f"Quantity: {sale[2]}", 
                    f"Total: R{sale[3]:.2f}", 
                    f"Date: {sale[4]}")





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

inventory.add_product(hoodie)
inventory.add_product(tshirt)
inventory.add_product(cargo_pants)
inventory.add_product(denim_jeans)
inventory.add_product(shirt)
inventory.add_product(sweater)
inventory.add_product(windbreaker)
inventory.add_product(bomber_jacket)
inventory.add_product(baseball_cap)
inventory.add_product(bucket_hat)
inventory.add_product(beanie)
inventory.add_product(panel_cap)
inventory.add_product(wide_leg_pants)
inventory.add_product(track_pants)
inventory.add_product(tank_top)

print("Inventory after adding products:", inventory.total_products())

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

