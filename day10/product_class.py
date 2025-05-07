class Product:
    def __init__(self, name, price, quantity):
        """Initializes a Product object with name, price, and quantity."""
        self.name = name
        self.price = price
        self.quantity = quantity

prod1 = Product("Laptop", 1200.00, 10)
print(f"Product : {prod1.name}")
print(f"Price: ${prod1.price:.2f}")
print(f"Quantity: {prod1.quantity}")