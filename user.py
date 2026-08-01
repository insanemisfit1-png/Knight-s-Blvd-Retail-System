class User:
    def __init__(self, username, password, role):
        self.username   =   username
        self.password   =   password
        self.role   =   role
        def login(self, username, password):
            return self.username    ==  username and self.password   ==   password
        def display_user(self):
            print(f"Username:   {self.username}")
            print(f"Role:   {self.role}")
