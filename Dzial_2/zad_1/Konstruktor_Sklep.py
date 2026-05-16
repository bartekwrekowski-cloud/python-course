import random

class Product:
    def __init__(self, name,category,price):
        self.name = name
        self.category = category
        self.price = int(price)

class Order:
    def __init__(self, first_name,last_name, product_list = None):
        self.first_name = first_name
        self.last_name = last_name
        if product_list is None:
            self.product_list = []
        else:
            self.product_list = product_list

        total_price = 0
        for product in product_list:
            total_price += product.price
        self.total_price = total_price



class Apple:
    def __init__(self, species_name, size,price):
        self.species_name = species_name
        self.size = size
        self.price = int(price)

class Potato:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = int(price)

def show_order(new_order):
    print(f"Zamowienie zlozyl: {new_order.first_name} {new_order.last_name}, łączna kwota zamówienia to {new_order.total_price} PLN.")

# def random_order():
#     number_of_products = random.randint(1,15)
#     products = []
#
#     for product_number in range(number_of_products):
#         p_name = f"Product name: {product_number}"
#         p_category = f"Fruits/Vegetables"
#         p_price = random.randint(5,50)
#         products.append(Product(p_name,p_category,p_price))
#
#     order_random = Order(
#         first_name = "Random",
#         last_name = "Client",
#         product_list = products
#     )
#     return order_random

def execute_example():

    apple_1 = Apple("green", size = "small", price = 20)
    apple_2 = Apple("red", size = "medium", price = 10)
    potato_1 = Potato("young", size = "small", price = 5)
    potato_2 = Potato("sweet", size = "big", price = 15)
    product_1 = Product("milk","protein",30)
    product_2 = Product("cola","drink",9)
    #new_order = Order("Bartek","Rekowski",[product_1,product_2,apple_2,potato_1])

    # new_order = random_order()
    # show_order(new_order)

if __name__ == "__main__":
    execute_example()