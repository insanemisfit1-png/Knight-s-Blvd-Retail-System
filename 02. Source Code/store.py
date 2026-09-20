from itertools import product
class Store:
    def __init__(self, name, inventory, db):
        self.name = name
        self.inventory = inventory
        self.db = db

    def add_product(self, product):
        self.inventory.add_product(product)

    def display_inventory(self):
        print(f"----- Welcome to {self.name}  -----")
        self.inventory.display_inventory()

    def welcome(self):
        print(f"Welcome to {self.name}!")
        print("We 're glad to have you here.")
        print(f"")

    def sell_product(self, customer_name, product_name, quantity):
        print("Store Inventory Count:", self.inventory.total_products())  # Debugging line
        print("    store received:", repr(product_name))  # Debugging line
        if not self.db.customer_exists_by_name(customer_name):
             print("Customer not found")
             return
        for product in self.inventory.products:
            print("    Inventory product:", repr(product_name))  # Debugging line  
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
        product = None
        for item in self.inventory.products: 
            print("Inventory product:", repr(item.name))  # Debugging line
            print("User entered:", repr(product_name))  # Debugging line
            print("Comparing:", repr(item.name.strip().casefold() == product_name.strip().casefold()))
            if item.name.strip().casefold() == product_name.strip().casefold():
                product = item
                break
        if  product is None:
                    print("Product not found")
                    return
        print("    Stock:", product.stock)  # Debugging line
        if product.stock < quantity:
                print(f"Insufficient stock for {product.name}. " f"Available stock: {product.stock}" )
                return
        total_price = product.price * quantity
        product.stock -= quantity
        self.db.save_sale(
             customer_name, 
             product_name, 
             quantity, 
             total_price)
        print(f"Sold {quantity} of {product.name}." f" Total price: R{total_price}")
        print(f"Remaining stock for {product.name}:" f" {product.stock}")
                
    def total_products(self):
        return self.inventory.total_products()
    def total_price(self):
        total = int(0)
        for product in self.inventory.products:
            total += product.price * product.stock
        return total      

    def view_products(self):
        products = self.db.load_products()

        for product in products:
            print(product)
