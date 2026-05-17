import random

from Shop.product import Product

class Order:
    def __init__(self, first_name,last_name, order_elements = None):
        self.first_name = first_name
        self.last_name = last_name
        if order_elements is None:
            self.order_elements = []
        else:
            self.order_elements = order_elements

        self.order_elements = order_elements if order_elements is not None else []
        self.total_price = self.calculate_total_price()

    def calculate_total_price(self):
         total_price = 0
         for product in self.order_elements:
             total_price += product.price
         return total_price

    def show_order(self):
        print(f"Zamowienie zlozyl: {self.first_name} {self.last_name}, " f"łączna kwota zamówienia to {self.total_price} PLN.")
        for product in self.order_elements:
            product.print_product()



    @classmethod
    def random_order(cls):
        number_of_products = random.randint(1, 15)
        products = []

        for product_number in range(number_of_products):
            p_name = f"Product name: {product_number}"
            p_category = f"Fruits/Vegetables"
            p_price = random.randint(5, 50)
            products.append(Product(p_name, p_category, p_price))

        order_random = cls(
            first_name="Random",
            last_name="Client",
            order_elements=products
        )
        return order_random
