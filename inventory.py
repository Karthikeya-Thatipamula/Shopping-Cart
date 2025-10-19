# inventory.py
# Creates a store inventory with categories and products

# Initialize inventory with 3 categories and 2 products each
inventory = [
    {"category": "Fruit", "products": [
        {"name": "Apple", "price": 0.5, "quantity": 100},
        {"name": "Banana", "price": 0.3, "quantity": 150}
    ]},
    {"category": "Dairy", "products": [
        {"name": "Milk", "price": 3.0, "quantity": 50},
        {"name": "Cheese", "price": 5.0, "quantity": 30}
    ]},
    {"category": "Snacks", "products": [
        {"name": "Chips", "price": 2.0, "quantity": 80},
        {"name": "Cookies", "price": 2.5, "quantity": 60}
    ]}
]

# Filter products by category using list comprehension
fruit_products = [p for category in inventory for p in category["products"] if category["category"] == "Fruit"]

if __name__ == "__main__":
    print(fruit_products)