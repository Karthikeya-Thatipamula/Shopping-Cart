# checkout.py
# Implements checkout with bill calculation and discounts

class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

class Basket:
    def __init__(self):
        self.items = []
    
    def add_product(self, product, quantity):
        if quantity <= product.quantity:
            self.items.append((product, quantity))
            product.quantity -= quantity
        else:
            raise ValueError(f"Not enough stock for {product.name}. Available: {product.quantity}")
    
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
    discount = float(input("Enter discount percentage (0 for none): ")) / 100
    return total * (1 - discount)

if __name__ == "__main__":
    apple = Product("Apple", 0.5, 100, "Fruit")
    basket = Basket()
    basket.add_product(apple, 10)
    basket.checkout()