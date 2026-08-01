class Store:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory()
        store = Store("Knight's Blvd", inventory)

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
        product = self.inventory.search_by_name(product_name)
        if product is  not None:
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
        if  product.reduce_stock( quantity): order = Order(self.generate_order_id, customer, product, quantity)
        receipt = receipt(order)
        receipt.generate_receipt()

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

    def welcome(self):
        print(f"Welcome to {self.name}!")