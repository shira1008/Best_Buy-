class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("The name cannot be empty")
        if price < 0:
            raise ValueError("The price have to be positive")
        if quantity < 0:
            raise ValueError("The quantity have to be positive")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("The quantity have to be positive and bigger than 0")
        # out of stock
        if not self.is_active():
            raise ValueError(f"This product is out of stock")

        # if the user want to buy more than the store have
        if quantity > self.quantity:
            raise ValueError(f"You asked for {quantity} but there are only {self.quantity} available")

        self.quantity -= quantity
        total_price = self.price * quantity

        if self.quantity == 0:
            self.set_quantity(0)

        return total_price
