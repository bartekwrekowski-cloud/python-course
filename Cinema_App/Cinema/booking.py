from .screening import Screening

class Booking:
    def __init__(self,customer_name: str,screening: Screening,seats_count: int):
        self.customer_name = customer_name
        self.screening = screening
        self.seats_count = seats_count

        self.total_cost: float = round(seats_count * self.screening.movie.price, 2)

    def print_ticket(self):
        movie = self.screening.movie

        print("\n" + "=" * 46)
        print("          BILET ELEKTRONICZNY - KINO          ")
        print("=" * 46)
        print(f" Klient:         {self.customer_name}")
        print(f" Film:           '{movie.title}'")
        print(f" Czas trwania:   {movie.duration} min")
        print("-" * 46)
        print(f" Sala:           {self.screening.room_name}")
        print(f" Godzina seansu: {self.screening.time}")
        print(f" Liczba miejsc:  {self.seats_count} szt.")
        print("-" * 46)
        print(f" DO ZAPŁATY:     {self.total_cost} PLN")
        print("=" * 46)
        print("   Dziękujemy za zakup i życzymy udanego seansu!   ")
        print("=" * 46 + "\n")
