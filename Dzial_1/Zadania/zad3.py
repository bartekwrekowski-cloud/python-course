
from calculations import zad3_1 as calculations

kapital_poczatkowy = int(input(f"Podaj kapital poczatkowy: "))
oprocentowanie = int(input(f"Podaj oprocentowanie: "))
okres_trwania = int(input(f"Podaj okres trwania: "))

wartosc = calculations.oblicz_lokate(kapital_poczatkowy,oprocentowanie,okres_trwania)
print(f"Wartosc lokaty wynosi: {wartosc}")