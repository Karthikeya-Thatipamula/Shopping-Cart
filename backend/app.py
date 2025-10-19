from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
import os

app = Flask(__name__, static_folder='../frontend')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key') # Add a secret key for sessions

database_url = os.environ.get('DATABASE_URL')
# Render's DATABASE_URL starts with postgres://, but SQLAlchemy needs postgresql://
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

# Use the production database URL if available, otherwise fall back to local SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = database_url or f"sqlite:///{os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance', 'store.db')}"
db = SQLAlchemy(app)
CORS(app, supports_credentials=True) # supports_credentials is required for session cookies
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'category': self.category
        }

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    product = db.relationship('Product')

    def to_dict(self):
        return {
            'id': self.id,
            'product': self.product.to_dict(),
            'quantity': self.quantity
        }

with app.app_context():
    db.create_all()

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    user = User(username=data['username'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({'message': 'Login successful', 'user': {'id': user.id, 'username': user.username}})
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/api/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'})

@app.route('/api/current_user', methods=['GET'])
def get_current_user():
    if current_user.is_authenticated:
        return jsonify({'user': {'id': current_user.id, 'username': current_user.username}})
    return jsonify({'user': None})

@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@app.route('/api/cart', methods=['GET'])
@login_required
def get_cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    return jsonify([item.to_dict() for item in cart_items])

@app.route('/api/cart', methods=['POST'])
@login_required
def add_to_cart():
    data = request.get_json()
    cart_item = CartItem(user_id=current_user.id, product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(cart_item)
    db.session.commit()
    return jsonify({'message': 'Item added to cart'})

@app.route('/api/cart/<int:item_id>', methods=['DELETE'])
@login_required
def remove_from_cart(item_id):
    cart_item = CartItem.query.get_or_404(item_id)
    if cart_item.user_id != current_user.id:
        return jsonify({'message': 'Unauthorized'}), 401
    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({'message': 'Item removed from cart'})

@app.route('/api/cart/<int:item_id>', methods=['PUT'])
@login_required
def update_cart_item(item_id):
    cart_item = CartItem.query.get_or_404(item_id)
    if cart_item.user_id != current_user.id:
        return jsonify({'message': 'Unauthorized'}), 401
    data = request.get_json()
    cart_item.quantity = data['quantity']
    db.session.commit()
    return jsonify({'message': 'Cart item updated'})

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
