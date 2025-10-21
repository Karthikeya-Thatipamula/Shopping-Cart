from app import app, db, Product, User, CartItem

inventory = [
    {"category": "Fruit", "products": [
        {"name": "Apple", "price": 0.5, "quantity": 100, "image_url": "https://via.placeholder.com/150/FF0000/FFFFFF?text=Apple"},
        {"name": "Banana", "price": 0.3, "quantity": 150, "image_url": "https://via.placeholder.com/150/FFFF00/000000?text=Banana"}
    ]},
    {"category": "Dairy", "products": [
        {"name": "Milk", "price": 3.0, "quantity": 50, "image_url": "https://via.placeholder.com/150/FFFFFF/000000?text=Milk"},
        {"name": "Cheese", "price": 5.0, "quantity": 30, "image_url": "https://via.placeholder.com/150/FFD700/000000?text=Cheese"}
    ]},
    {"category": "Snacks", "products": [
        {"name": "Chips", "price": 2.0, "quantity": 80, "image_url": "https://via.placeholder.com/150/A52A2A/FFFFFF?text=Chips"},
        {"name": "Cookies", "price": 2.5, "quantity": 60, "image_url": "https://via.placeholder.com/150/D2691E/FFFFFF?text=Cookies"}
    ]}
]

with app.app_context():
    db.create_all()
    # Delete data in the correct order to avoid foreign key violations
    CartItem.query.delete()
    User.query.delete()
    Product.query.delete()

    for category in inventory:
        for product_data in category['products']:
            product = Product(
                name=product_data['name'],
                price=product_data['price'],
                quantity=product_data['quantity'],
                category=category['category'],
                image_url=product_data['image_url']
            )
            db.session.add(product)
    db.session.commit()
