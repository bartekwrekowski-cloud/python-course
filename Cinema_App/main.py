from Cinema.screening import Screening
from Cinema.booking import Booking

def get_seans_number() -> int:
    while True:
        try:
            wybor = int(input("Wybierz numer seansu (1-3): "))
            if 1 <= wybor <= 3:
                return wybor
            print("Błąd: Wybierz liczbę z zakresu od 1 do 3!")
        except ValueError:
            print("Błąd: Musisz podać liczbę całkowitą!")

def pobierz_liczbe_biletow() -> int:
    while True:
        try:
            liczba = int(input("Ile biletów chcesz zarezerwować?: "))
            if liczba > 0:
                return liczba
            print("Błąd: Liczba biletów musi być większa od 0!")
        except ValueError:
            print("Błąd: Musisz podać liczbę całkowitą!")

def run_cinema_wizard():
    print("=========================================")
    print("   WITAMY KLIENTA W SYSTEMIE KINA   ")
    print("=========================================\n")
    seanse = [
        Screening.generate_random_screening(room="Sala Trójwymiarowa", time="15:30"),
        Screening.generate_random_screening(room="Sala Kameralna", time="18:00"),
        Screening.generate_random_screening(room="Sala IMAX", time="21:15")
    ]

    print("--- AKTUALNY REPERTUAR ---")
    for index, seans in enumerate(seanse, start = 1):
        print(f"{index}. Film:  '{seans.movie.title}' | {seans.room_name} | Godzina: {seans.time} "
              f"| Wolne miejsca: {seans.available_seats} | Cena: {seans.movie.price} PLN")

    wybrany_indeks = pobierz_liczbe_biletow() - 1
    wybrany_seans = seanse[wybrany_indeks]

    klient = input("Podaj swoje imię i nazwisko: ".strip())
    while not klient:
        klient = input("Imię i nazwisko nie może  być puste. Podaj dane: ").strip()

    liczba_biletow = get_seans_number()

    print("\n[System]: Przetwarzanie rezerwacji...")
    if wybrany_seans.reserve_seats(liczba_biletow):
        rezerwacja = Booking(customer_name=klient,screening=wybrany_seans,seats_count=liczba_biletow)
        rezerwacja.print_ticket()
    else:
        print("[System]: Rezerwacja odrzucona. Spróbuj ponownie dla mniejszej liczby miejsc.")

if __name__ == "__main__":
    run_cinema_wizard()


