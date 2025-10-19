import logging
from app import app, db, Product

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

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

def setup_database():
    with app.app_context():
        logger.info("Starting database setup...")

        # Drop all tables first to ensure a clean slate
        logger.info("Dropping all existing tables...")
        db.drop_all()

        # Create all tables defined in the models
        logger.info("Creating all new tables...")
        db.create_all()

        logger.info("Seeding the database with initial products...")
        # Check if products already exist to avoid duplicates, just in case
        if Product.query.first() is None:
            for category_data in inventory:
                for product_data in category_data['products']:
                    product = Product(
                        name=product_data['name'],
                        price=product_data['price'],
                        quantity=product_data['quantity'],
                        category=category_data['category']
                    )
                    db.session.add(product)
            db.session.commit()
            logger.info(f"Successfully added {Product.query.count()} products to the database.")
        else:
            logger.info("Products already exist in the database. Skipping seeding.")

        logger.info("Database setup completed successfully!")

if __name__ == '__main__':
    setup_database()
