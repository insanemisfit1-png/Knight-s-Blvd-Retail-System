class Analytics:
    def __init__(self):
        self.total_sales = 0
        self.total_revenue = 0
    def record_sale(self, quantity, total):
        self.total_sales += quantity
        self.total_revenue += total
        def display_report(self):
            print("\n=====  SALES REPORT    =====")
            print(f"Products Sold:  { self.total_sales}")
            print(f"Revenue:    R{self.total_revenue:.2f}")