# customer_management.py
# Manages customer data and loyalty programs

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
    
    def add_points(self, points):
        self.loyalty_points += points

def greet_customer(customer_id, customers):
    if customer_id in customers:
        print(f"Welcome back, {customers[customer_id]['name']}!")
    else:
        print("Welcome, new customer!")

def offer_loyalty(customer_id, name, phone, customers):
    if customer_id not in customers:
        choice = input("Join our loyalty program? (yes/no): ").lower()
        if choice == "yes":
            new_id = f"C{len(customers) + 1:03d}"
            customers[new_id] = {"name": name, "phone": phone, "customer_id": new_id, "loyalty_points": 0}
            print(f"Welcome to the loyalty program, {name}! Your ID is {new_id}.")
        else:
            print("No problem, we’ll offer again next time!")

if __name__ == "__main__":
    customers = {
        "C001": {"name": "John", "phone": "123-456-7890", "customer_id": "C001", "loyalty_points": 0}
    }
    greet_customer("C001", customers)
    offer_loyalty("C002", "Jane", "987-654-3210", customers)