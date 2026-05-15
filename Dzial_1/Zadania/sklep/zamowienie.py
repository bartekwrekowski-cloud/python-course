from turtledemo.paint import switchupdown

from . import magazyn

def utworz_zamowienie(owoc,ilosc):

    if owoc not in magazyn.magazyn:
        print(f"Nie mamy owocu '{owoc}' w ofercie")
        return None

    if ilosc > magazyn.magazyn[owoc]["ilość"]:
        print("Nie mamy takiej liczby owocow")
        return None

    magazyn.magazyn[owoc]["ilość"] -= ilosc

    zamowienie = {
        "produkt": owoc,
        "ilosc": ilosc,
        "cena": magazyn.magazyn[owoc]["cena"] * ilosc
    }

    return zamowienie