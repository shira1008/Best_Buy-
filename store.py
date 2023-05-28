import products


class Store:
    def __init__(self, product_list):
        self.products = product_list

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total_quantity_counter = 0
        for product in self.products:
            total_quantity_counter += product.get_quantity()
        return total_quantity_counter

    def get_all_products(self):
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_cost = 0
        for product, quantity in shopping_list:
            total_cost += product.buy(quantity)
        return total_cost
