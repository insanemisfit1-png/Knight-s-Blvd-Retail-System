
Size = "Medium"
Price = "799.99"
Color = "Black"
Style = "Streetwear"
Age = "22"
Name = "Bhlomingtn"


class Customer:
    def __init__(self, Name, Size, Order, Price):
        self.name = Name
        self.size = Size
        self.order = Order
        self.price = Price

    def greet(self):
        print(f"Welcome to Knight's Blvd, {self.name}!")

        

    def show_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Order: {self.order}")
        print(f"Price: ${self.price}")      

    def display_profile(self):
        print("Customer Name:", self.name)
        print("Size:", self.size)
        print("Order:", self.order)
        print("Price:", self.price)





class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
       
       
  

    def display_inventory(self):
        print("----- Inventory -----")
        for product in self.products:
            product.display()
        print("---------------------")  
        print(f"")
        print(f"")  

    def total_products(self)->int:
        return len(self.products)

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None    
    
    def search_by_name(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
            return None

    def search_by_color(self, color):
        results = []

        for product in self.products:
            if product.color.lower() == color.lower():
                results.append(product)

                return results








class Product:
    def __init__(self, name, size, price, color, style, stock):
        self.name = name
        self.size = size
        self.price = price
        self.color = color
        self.style = style
        self.stock = stock

    def display(self):
        print(f"-----  Knight's Blvd  -----")
        print(f"Product Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Price: R{self.price}")
        print(f"Color: {self.color}")
        print(f"Style: {self.style}")
        print(f"Stock: {self.stock}") 

        hoodie = Product("Black Hoodie", "Medium", 799.99, "Black", "Streetwear", 20)
        tshirt = Product("White T-shirt", "Large", 499.99, "White", "Casual", 35)   





product_names = ["hoodie", "tshirt", "cargo_pants", "denim_jeans", "shirt", "sweater", "windbreaker", "bomber_jacket", "baseball_cap", "bucket_hat", "beanie", "panel_cap", "wide_leg_pants", "track_pants", "tank_top"
            ]
colors = ["Black", "White", "Beige", "Grey", "Navy Blue", "Olive Green", "Burgundy", "Mustard Yellow", "Rust Orange", "Charcoal Grey"]
styles = ["Streetwear", "Casual", "Athleisure", "Minimalist", "Vintage", "Preppy", "Bohemian", "Grunge", "Sporty", "Chic"]
products = []
for name in product_names:
    for color in colors:                
        for style in styles:
            for size in ["XS", "S", "M", "L", "XL", "XXL"]:
                price = 799.99
                stock = 20
                product = Product(name, size, price, color, style, stock)
                products.append(product)

                

            

order = products[4]
print(products[4])




def display_product_info(self):
        print(f"Product Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Price: R{self.price}")
        print(f"Color: {self.color}")
        print(f"Style: {self.style}")
        print(f"Stock: {self.stock}")

def show_details(self):
        print(f"Product: {self.name}")
        print(f"Size: {self.size}")
        print(f"Price: R{self.price}")
        print(f"Color: {self.color}")
        print(f"Style: {self.style}")
        print(f"In Stock: {self.stock}")   
        
     
def is_in_stock(self):
        return self.stock > 0

def reduce_stock(self, quantity):
    if self.stock >= quantity:
        self.stock -= quantity
        return True
    else:
        print("Not enough stock available."
        )
        return False

class Store:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()

    def add_product(self, product):
        self.inventory.add_product(product)

    def display_inventory(self):
        print(f"----- Welcome to {self.name}  -----")
        self.inventory.display_inventory()

    def welcome(self):
        print(f"Welcome to {self.name}!")
        print("We 're glad to have you here.")
        print(f"")

    def sell_product(self, product_name, quantity):
        product = self.inventory.find_product(product_name)
        if product is not None:
            if product.stock >= quantity:
                total_price = product.price * quantity
                product.stock -= quantity
                print(f"Sold {quantity} of {product.name}. Total price: R{total_price}")
            else:
                print(f"Insufficient stock for {product.name}. Available stock: {product.stock}")
        if product is None:
            print("Product not found")
            return
        if product.stock < quantity:
            print("Sorry, we only have", product.stock, "left")
            return
            product.stock -= quantity
            print("Sale successful!")
            print("Remaining stock:", product.stock)

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return
    def sell_product(self, product, quantity):
        if product.reduce_stock( quantity):
            total = product.price * quantity 
            print("=====   RECEIPT  =====")
            print(f"Product : {product.name}")
            print(f"Quantity: {quantity}")
            print(f"Price: R{product.price:.2f}")
            print(f"Total : R {total:.2f}")
            print(f"Stock Left : {product.stock}")
            print("========================")
            return total 


    def total_products(self):
        return self.inventory.total_products()
    def total_price(self):
        total = int(0)
        for product in self.inventory.products:
            total += product.price * product.stock
        return total      


store = Store("Knight's Blvd")
store.welcome()

class Receipt:
    def __init__(self, order):
        self.order = order

    def generate_receipt(self):
        print(f"=====")
        print(f"      KNIGHT'S BLVD      ")
        print(f"=====")
        print(f"Order ID: {self.order}")
        print(f"Customer: {self.order.customer.name}")
        print(f"Product: {self.order.product.name}")
        print(f"Quantity: {self.order.quantity}")
        total = self.order.product.price * self.order.quantity
        print(f"Total Price: R{total}")
        print(f"===========================") 
        print(f"Thank you for your purchase!")
        print(f"===========================")
        print(f"")


    def save_receipt(self):
        total = self.order.product.price * self.order.quantity
        with open("receipts.txt","a") as file:
            file.write("=====\n")
            file.write("KNIGHT'S BLVD\n")
            file.write(f"Customer: {self.order.customer.name}\n")
            file.write(f"Product:{self.order.product.name}\n")
            file.write(f"Quantity:{self.order.quantity.name}\n")
            file.write(f"Total Price:  R {total}\n")
            file.write(f"Thank you for your purchase!\n")
            file.write(f"=====\n\n")
        








customer1 = Customer("Bhlomingtn", "Medium", "Black Hoodie", "799.99")
hoodie = Product("Black Hoodie", "Medium", 799.99, "Black", "Streetwear", 20)
jeans = Product("Blue Jeans", "Medium", 699.99, "Blue", "Casual", 30)
customer2 = Customer("John Doe", "Large", "Beige Hoodie", "899.99")
hoodie2 = Product("Beige Hoodie", "Large", 899.99, "Beige", "Casual", 15)
customer3 = Customer("Jane Smith", "Small", "White T-shirt", "499.99")
tshirt3 = Product("White T-shirt", "Small", 499.99, "White", "Casual", 25)
customer4 = Customer("Alice Johnson", "Medium", "Blue Jeans", "699.99")
jeans4 = Product("Blue Jeans", "Medium", 699.99, "Blue", "Casual", 30)
customer5 = Customer("Bob Williams", "Large", "Black T-shirt", "599.99")
tshirt5 = Product("Black T-shirt", "Large", 599.99, "Black", "Casual", 20)
jeans5 = Product("Blue Jeans", "Medium", 699.99, "Blue", "Casual", 30)
customer6 = Customer("Carol Davis", "Small", "White Hoodie", "799.99")
hoodie6 = Product("White Hoodie", "Small", 799.99, "White", "Streetwear", 15)
jeans6 = Product("Black Jeans", "Medium", 699.99, "Black", "Casual", 30)


   
store.add_product(hoodie)
customer1.name
customer1.greet()
customer1.order
customer1.size
customer1.price
hoodie = store.inventory.find_product("Black Hoodie")
if hoodie:
    print(f"Product found: {hoodie.name}, Size: {hoodie.size}, Price: R{hoodie.price}")
customer1.show_details()
order1 = Order(customer1, hoodie, 1)
order1.display_order()
order1.checkout()
receipt = Receipt(order1)
receipt.generate_receipt()


store.add_product(hoodie2)
customer2.name
customer2.greet()
customer2.order
customer2.size
customer2.price 
customer2.show_details()
order2 = Order(customer2, hoodie2, 1)
order2.display_order()
order2.checkout()
receipt = Receipt(order2)
receipt.generate_receipt( )



store.add_product(tshirt3)
customer3.name
customer3.greet()
customer3.order
customer3.size
customer3.price
customer3.show_details()
order3 = Order(customer3, tshirt3, 1)
order3.display_order()
order3.checkout()
receipt = Receipt(order3)
receipt.generate_receipt( )



store.add_product(jeans4)
customer4.name
customer4.greet()
customer4.order
customer4.size
customer4.price
customer4.show_details()
order4 = Order(customer4, jeans4, 3)
order4.display_order()
order4.checkout()
receipt = Receipt(order4)
receipt.generate_receipt( )


store.add_product(tshirt5)
customer5.name
customer5.greet()
customer5.order
customer5.size
customer5.price
customer5.show_details()
order5 = Order(customer5, tshirt5, 1)
order5.display_order()
order5.checkout()
receipt = Receipt(order5)
receipt.generate_receipt( )




store.add_product(hoodie6)
customer6.name
customer6.greet()
customer6.order
customer6.size
customer6.price
customer6.show_details()
order6 = Order(customer6, hoodie6, 1)
order6.display_order()
order6.checkout()
receipt = Receipt(order6)
receipt.generate_receipt( )


print(Inventory().total_products())
store.display_inventory()

store.sell_product("Black Hoodie", 1)
store.sell_product("Beige Hoodie", 1)
store.sell_product("White T-shirt", 3)
store.sell_product("Blue Jeans", 5)
store.sell_product("Black T-shirt", 2)
store.sell_product("White Hoodie", 1)




inventory = store.inventory
result = inventory.search_by_name("Black Hoodie")

if result:
    result.display()
else:
    print("Product not found.")

black_products = inventory.search_by_color("Black")
for product in black_products:
    product.display()

jeans6 = Product("Black Jeans", "Medium", 699.99, "Black", "Casual", 30)


if reduce_stock( quantity ): 
    print(f"Sold { quantity}{hoodie.name}(s).") 
    print(f"Remaining stock: {hoodie.stock}")

        update_stock(hoodie)
        update_stock(tshirt)
        update_stock(cargo_pants)
        update_stock(denim_jeans)
        update_stock(shirt)
        update_stock(sweater)
        update_stock(windbreaker)
        update_stock(bomber_jacket)
        update_stock(baseball_cap)
        update_stock(bucket_hat)
        update_stock(beanie)
        update_stock(panel_cap)
        update_stock(wide_leg_pants)
        update_stock(track_pants)
        update_stock(tank_top)








