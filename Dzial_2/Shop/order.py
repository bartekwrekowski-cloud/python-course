import random

from Shop.product import Product

class Order:
    def __init__(self, first_name,last_name, product_list = None):
        self.first_name = first_name
        self.last_name = last_name
        if product_list is None:
            self.product_list = []
        else:
            self.product_list = product_list

        self.product_list = product_list if product_list is not None else []

        total_price = 0
        for product in self.product_list:
            total_price += product.price
        self.total_price = total_price

    def show_order(self) -> None:
        print(f"Zamowienie zlozyl: {self.first_name} {self.last_name}, " f"łączna kwota zamówienia to {self.total_price} PLN.")
        for product in self.product_list:
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
            product_list=products
        )
        return order_random
