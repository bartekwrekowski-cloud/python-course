class Movie:

    def __init__(self,title,duration,price):
            self.title = title
            self.duration = int(duration)
            self.price = float(price)

    def print_info(self):
        print(f"Title: {self.title} [{self.duration} min] | Price: {self.price} PLN.")
