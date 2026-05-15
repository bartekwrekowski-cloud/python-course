import math

def oblicz_przeciwprastokatna(a,b):
    c = pow(a,2) + pow(b,2)
    wynik = math.sqrt(c)
    return wynik

print(f"Przeciwprostokatna wynosi: ", oblicz_przeciwprastokatna(3,4))