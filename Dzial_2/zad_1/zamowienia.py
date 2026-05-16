import doctest


class Produkt:
    pass

class Zamowienia:
    pass

class Jabłko:
    pass

class Ziemniaki:
    pass


if __name__ == "__main__":

    jabłko_zielone = Jabłko()
    jabłko_czerwone = Jabłko()

    ziemniak_zwykły = Ziemniaki()
    ziemniak_słodki = Ziemniaki()

    print("type jabłko_zielone: ", type(jabłko_zielone))
    print("type jabłko_czerwone: ", type(jabłko_czerwone))
    print("type ziemniak_zwykły: ", type(ziemniak_zwykły))
    print("type ziemniak_słodki: ", type(ziemniak_słodki))

    zamowienia = [Zamowienia(), Zamowienia(), Zamowienia(), Zamowienia(), Zamowienia()]
    print(zamowienia)


    produtky = {
        "Ryż": Produkt(),
        "Jajka": Produkt(),
        "Masło": Produkt(),
        "Makaron": Produkt(),
        "Mleko": Produkt()
    }

    print("produtky: ", produtky)