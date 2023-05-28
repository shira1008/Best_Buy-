from abc import ABC, abstractmethod


class Promotion(ABC):
    # class variable (member) for name
    name = ""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        discount_amount = product.price * self.percent / 100
        new_price = product.price - discount_amount
        total_price = new_price * quantity
        return total_price


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        full_price_items = quantity // 2  # how many items priced at the full price
        half_price_items = (
            quantity - full_price_items
        )  # how many items priced at half the price

        total_price = (full_price_items * product.price) + (
            half_price_items * (product.price / 2)
        )
        return total_price


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        full_price_items = quantity // 3 * 2
        total_price = full_price_items * product.price
        return total_price
