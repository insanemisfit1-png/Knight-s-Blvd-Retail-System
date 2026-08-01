class Receipt:
    def __init__(self, order):
        self.order = order
        
    def generate_receipt(self):
        print(f"==========")
        print(f"      KNIGHT'S BLVD      ")
        print(f"==========")
        print(f"Order ID: {self.order.order_id}")
        print(f"Customer: {self.order.customer.name}")
        print(f"Product: {self.order.product.name}")
        print(f"Quantity: {self.order.quantity}")
        print(f"Price: R{self.order.product.price:.2f}")
        print(f"Total: R{self.order.calculate_total():.2f}")
        print(f"Status: {self.order.status}")
        print(f"Date: {self.order.timestamp}")
        print(f"===========================") 
        print(f"Thank you for your purchase!")
        print(f"===========================")
    def save_receipt(self):
        self.order.calculate_total()
        with open("receipts.txt","a") as file:
            file.write("=====\n")
            file.write("KNIGHT'S BLVD\n")
            file.write(f"Customer: {self.order.customer.name}\n")
            file.write(f"Product:{self.order.product.name}\n")
            file.write(f"Quantity:{self.order.quantity}\n")
            file.write(f"Total Price:  R {self.order.calculate_total}\n")
            file.write(f"Date:{self.order.timestamp.strftime('%d/%m/%Y')}")
            file.write(f"Time:   {self.order.timestamp.strftime('%H:%M:%S')}")
            file.write(f"Thank you for your purchase!\n")
            file.write(f"=====\n\n")
