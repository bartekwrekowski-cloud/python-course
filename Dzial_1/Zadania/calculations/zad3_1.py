def oblicz_lokate(kapital_poczatkowy,oprocentowanie,okres_trwania):
    wynik = kapital_poczatkowy*(1+oprocentowanie/100)**okres_trwania
    return wynik