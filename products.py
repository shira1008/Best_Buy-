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
        self.promotion = None

        # for the promotion class

    def get_promotion(self):
        return self.promotion

        # for the promotion class

    def set_promotion(self, promotion):
        self.promotion = promotion

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
        if self.promotion:
            promotion_info = f", Promotion: {self.promotion.name}"
        else:
            promotion_info = ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

    def buy(self, quantity):
        if quantity <= 0:
            raise ValueError("The quantity have to be positive and bigger than 0")
        # out of stock
        if not self.is_active():
            raise ValueError(f"This product is out of stock")

        # if the user want to buy more than the store have
        if quantity > self.quantity:
            raise ValueError(
                f"You asked for {quantity} but there are only {self.quantity} available"
            )

        # check if have promotion, if have handle this with the changed price:
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity

        if self.quantity == 0:
            self.set_quantity(0)

        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        pass

    def show(self):
        return f"{self.name}, Price: {self.price}"

    def buy(self, quantity=0):
        total_price = self.price
        return total_price


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        return f"{self.name}, Price: {self.price}"

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"products can only be purchased {self.maximum} times")
        return super().buy(quantity)
