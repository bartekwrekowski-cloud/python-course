class Product:
    def __init__(self, name,category,price):
        self.name = name
        self.category = category
        self.price = int(price)

    def print_product(self):
        print(f"Nazwa: {self.name} | Kategoria: {self.category}  | Cena: {self.price}/s")