class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def product_inventory(self):
        print("----- Inventory -----")
        for product in self.products: product.display()
        print("---------------------")  
        print(f"")  

    def total_products(self)->int:
        return len(self.products)

    def find_product(self, name):
        for product in self.products:
            print("    Comparing:", repr(product.name), "WITH:", repr(name))  # Debugging line
            if product.name.strip().casefold() == name.strip().casefold():
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
                   
    def search_by_size(self, size):  
        results = []
        for product in self.products:
                if product.size.lower() == size.lower():
                    results.append(product)
                return results
        
    def search_by_style(self, style):  
        results = []
        for product in self.products:
            if product.style.lower() == style.lower():
                results.append(product)
            return results
            
    def search_by_price(self, max_price):  
        results = []
        for product in self.products:
            if product.price <= max_price:
                results.append(product)
            return results     
                          
    def remove_product(self, product_name):
        for product in self.products:
            if product_name.strip().casefold() == product_name.strip().casefold():
                self.products.remove(product)
                return product
            
        return None

    def update_product(self, product_name, new_name=None, new_price=None, new_stock=None):
        product = self.search_by_name(product_name)
        if product is None:
            return None
        if new_name is not None:
            product.name = new_name
        if new_price is not None:
            product.price = new_price
        if new_stock is not None:
            product.stock = new_stock

        return product

    def total_stock(self):
        pass

    def low_stock_products(self):
        pass