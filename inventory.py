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
            results.append(product)
            return results
        
    def search_by_size(self, size):  
            results = []
            for product in self.products:
                results.append(product)
                return results

    def search_by_category(self, category):  
            results = []
            for product in self.products:
                results.append(product)
                return results

    def search_by_prize(self, prize):  
            results = []
            for product in self.products:
                results.append(product)
                return results
        
    def remove_product(self):
        pass

    def update_product(self):
        pass

    def total_stock(self):
        pass

    def low_stock_products(self):
        pass
