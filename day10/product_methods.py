# day10/product_methods.py
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_details(self):
        """Prints product details."""
        print(f"Product: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}")

    def get_total_value(self):
        """Calculates and returns the total value of the stock."""
        return self.price * self.quantity

    def update_quantity(self, new_quantity):
        """Updates the product quantity."""
        if new_quantity >= 0:
            self.quantity = new_quantity
            print(f"Quantity of '{self.name}' updated to {self.quantity}.")
        else:
            print("Error: Quantity cannot be negative.")

prod1 = Product("Laptop", 1200.00, 10)
prod1.display_details()
total_val1 = prod1.get_total_value()
print(f"Initial total value: ${total_val1:,.2f}")

prod1.update_quantity(15)
total_val2 = prod1.get_total_value()
print(f"New total value: ${total_val2:,.2f}")

prod1.update_quantity(-5) # Test invalid quantity