# store_objects.py
# Defines Product, Customer, and Basket classes for the shopping cart

class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    
    def display(self):
        return f"{self.name} ({self.category}): ${self.price}, Stock: {self.quantity}"

class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.customer_id = None

class RegularCustomer(Customer):
    def __init__(self, name, phone, customer_id):
        super().__init__(name, phone)
        self.customer_id = customer_id
        self.loyalty_points = 0

class Basket:
    def __init__(self):
        self.items = []  # List of (product, quantity) tuples
    
    def add_product(self, product, quantity):
        self.items.append((product, quantity))

if __name__ == "__main__":
    apple = Product("Apple", 0.5, 100, "Fruit")
    customer = Customer("John", "123-456-7890")
    basket = Basket()
    basket.add_product(apple, 2)
    print(apple.display())