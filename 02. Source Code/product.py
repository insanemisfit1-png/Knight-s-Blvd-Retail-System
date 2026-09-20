class Product:
    def __init__(self, name, size, price, color, style, stock):
        self.name = name
        self.size = size
        self.price = price
        self.color = color
        self.style = style
        self.stock = stock

    def show_details(self):
        print(f"Product Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Price: R{self.price:.2f}")
        print(f"Color: {self.color}")
        print(f"Style: {self.style}")
        print(f"Stock: {self.stock}"
              )
        
    def is_in_stock(self):
            return self.stock > 0
    
    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        else:
            print(f"Only {self.stock} item(s) remaining.")
            return False 
        
    def __str__(self):
         return f"{self.name} ({self.size})   -    R{self.price:.2f}"
        



