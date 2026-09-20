from datetime import datetime
class Transaction:
    def __init__(self, 
            transaction_id,
            customer,
            employee,
            items,
            payment_method):
    self.transaction_id =   transaction_id
    self.customer   =   customer
    self.employee   =   employee
    self.items  =   items
    self.payment_method =   payment_method
    self.date   =   datetime.now()
    self.status     =   "Completed"

    def calculate_total(self):
        self.calculate_total    =   0
        for product, quantity in self.items:
            total += product.price * quantity
            return total

    def display_transaction(self):
        print("=====    TRANSACTION    =====")
        print(f"ID: {self.transaction_id}")
        print(f"Customer:   {self.customer.name}")
        print(f"Employee:   {self.employee}")
        print(f"Date:   {self.date}")
        for product, quantity in self.items:
            print(f"{product.name} * {quantity}")
        print(f"Payment:   {self.payment_method}")
        print(f"Status: {self.status}")
        print(f"Total:  R{self.calculate_total():.2f}")
        