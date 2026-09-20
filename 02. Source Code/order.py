from datetime import datetime
class Order:
    def __init__(self, order_id, customer, product, quantity):
        self.order_id = order_id
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.status = "Paid"
        self.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")

    def add_products(self, product, quantity): 
            self.product = product
            self.quantity = quantity  

               
    def remove_product(self, product):
        self.product.remove(product)
        self.products = []

        pass
    def calculate_total(self):
                        return self.product.price * self.quantity   
    def checkout(self):
        if self.product.stock >= self.quantity:
            total_price = self.product.price * self.quantity
            self.product.reduce_stock(self.quantity)
            return True
            print(f"Remaining stock for {self.product.name}: {self.product.stock}")
            print(f"Total:  R{total_price:.2f}")
        else:
            return False

    def cancel_order(self):
           self.status = "Cancelled"

    def display_order(self):
        print(f"=====   Order   =====")
        print(f"Customer: {self.customer.name}")            
        print(f"Order ID: {self.order_id}")
        print(f"Product: {self.product.name}")
        print(f"Status: {self.status}")
        print(f"Quantity: {self.quantity}")
        print(f"Date: {self.timestamp}")
        print(f"Price: R{self.calculate_total():.2f}")

    def order_id(self):
           return self.order_id