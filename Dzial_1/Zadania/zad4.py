from sklep.zamowienie import utworz_zamowienie


def uruchom_sklep()->None:

    print("Witaj w symulatorze sklepu")

    wybrany_owoc = input(f"Podaj jaki owoc chcesz kupić: ")
    wybrana_ilosc = int(input(f"Podaj ilość: "))

    zamowienie = utworz_zamowienie(wybrany_owoc, wybrana_ilosc)

    if zamowienie is not None:
        laczny_koszt = zamowienie["cena"]
        print(f"\nŁączny koszt Twoich zakupów to: {laczny_koszt} PLN.")
    else:
        print("\nZamówienie nie mogło zostać zrealizowane.")

if __name__ == "__main__":
    uruchom_sklep()