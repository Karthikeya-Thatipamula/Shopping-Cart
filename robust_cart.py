# robust_cart.py
# Enhances shopping cart with error handling and updates

inventory = [
    {"category": "Fruit", "products": [
        {"name": "Apple", "price": 0.5, "quantity": 100},
        {"name": "Banana", "price": 0.3, "quantity": 150}
    ]},
    # ... (other categories)
]

class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

class Basket:
    def __init__(self):
        self.items = []
    
    def add_product(self, product, quantity, inventory):
        if quantity <= product.quantity:
            self.items.append((product, quantity))
            product.quantity -= quantity
            update_inventory(inventory, product.name, quantity)
        else:
            raise ValueError(f"Not enough stock for {product.name}")
    
    def checkout(self):
        total = calculate_total(self)
        discounted_total = apply_discount(total)
        print("=== Receipt ===")
        for product, quantity in self.items:
            print(f"{product.name}: {quantity} x ${product.price} = ${product.price * quantity}")
        print(f"Total: ${total:.2f}")
        print(f"After Discount: ${discounted_total:.2f}")

def calculate_total(basket):
    total = 0
    for product, quantity in basket.items:
        total += product.price * quantity
    return total

def apply_discount(total):
    try:
        discount = float(input("Enter discount percentage (0 for none): ")) / 100
        if discount < 0 or discount > 1:
            raise ValueError("Discount must be between 0 and 100")
        return total * (1 - discount)
    except ValueError as e:
        print(f"Invalid input: {e}. Using no discount.")
        return total

def update_inventory(inventory, product_name, quantity):
    for category in inventory:
        for product in category["products"]:
            if product["name"] == product_name:
                if quantity <= product["quantity"]:
                    product["quantity"] -= quantity
                else:
                    raise ValueError(f"Not enough stock for {product_name}")

if __name__ == "__main__":
    apple = Product("Apple", 0.5, 100, "Fruit")
    basket = Basket()
    try:
        basket.add_product(apple, 10, inventory)
        print(inventory[0]["products"][0]["quantity"])
    except ValueError as e:
        print(e)