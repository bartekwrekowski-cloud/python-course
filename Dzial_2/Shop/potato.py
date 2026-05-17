class Potato:
    def __init__(self, species_name, size, price):
        self.species_name = species_name
        self.size = size
        self.price = int(price)

    def calculate_total_price(self,quantity):
        return quantity * self.price