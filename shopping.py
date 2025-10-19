# shopping.py
# Simulates shopping by adding products to a basket

# From Blog 1
inventory = [
    {"category": "Fruit", "products": [
        {"name": "Apple", "price": 0.5, "quantity": 100},
        {"name": "Banana", "price": 0.3, "quantity": 150}
    ]},
    # ... (other categories from Blog 1)
]

# From Blog 2
class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    
    def display(self):
        return f"{self.name} ({self.category}): ${self.price}, Stock: {self.quantity}"

class Basket:
    def __init__(self):
        self.items = []
    
    def add_product(self, product, quantity):
        if quantity <= product.quantity:
            self.items.append((product, quantity))
            product.quantity -= quantity
        else:
            raise ValueError(f"Not enough stock for {product.name}. Available: {product.quantity}")

def display_inventory(inventory):
    for category in inventory:
        print(f"Category: {category['category']}")
        for product in category['products']:
            print(f"  {product['name']}: ${product['price']}, Stock: {product['quantity']}")

if __name__ == "__main__":
    apple = Product("Apple", 0.5, 100, "Fruit")
    basket = Basket()
    display_inventory(inventory)
    try:
        basket.add_product(apple, 10)
        print(f"Added 10 {apple.name} to basket")
    except ValueError as e:
        print(e)