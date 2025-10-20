from app import app, db, Product, User, CartItem

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
                category=category['category']
            )
            db.session.add(product)
    db.session.commit()
