from .movie import Movie
import random

class Screening:

    def __init__(self, movie, room_name, time, available_seats = random.randint(15,40)):
        self.movie = movie
        self.room_name = room_name
        self.time = time
        self.available_seats = int(available_seats)

    def reserve_seats(self, count: int) -> bool:
        if count <= self.available_seats:
            self.available_seats -= count
            return True
        else:
            print("Not enough seats")
            return False

    @classmethod
    def generate_random_screening(cls, room: str, time: str):
        available_titles = ["Shrek", "Toy Story", "Epoka Lodowcowa"]
        random_title = random.choice(available_titles)
        random_duration = random.randint(90,180)
        random_price = random.randint(50,100)

        generated_movie = Movie(random_title,random_duration,random_price)
        return cls(movie = generated_movie, room_name = room, time = time)
