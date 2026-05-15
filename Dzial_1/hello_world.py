word = "Hello"
WIEK = 21
IMIE = "Bartek"
print(word + " " + IMIE)
print(IMIE)


if IMIE == "Bartek":
    print(IMIE)
else:
    print("Inne imie")

imiona = {"Mateusz", "Mikolaj", "Ania", "Karolina"}
for index, value in enumerate(imiona):
    print(index, value)

ludzie = {
    "Mateusz": [21],
    "Karolina": [15],
    "Ania": [17],
    "Mikolaj": [18]
}

wydatki = {120,300,250,3000,50,75}

liczby = {1,2,3,4,5,6,7,8,9,10}

oceny_przedmioty = {
    "Matematyka": [5,3,5,4],
    "Angielski": [5,3,5,6],
    "Historia": [5,3,5,4]
}

for key, value in ludzie.items():
    print(key, value)

for letter in IMIE:
    print(letter)


for number in range(11):
    print(number)


for koszt in wydatki:
    print(koszt)
    if koszt >= 1000:
        print("znaleziono drogi zakup: ")
        break

for index, imie in enumerate(imiona):
    if index % 2 != 0:
        continue
    print(imie)

def znajdz_najwyzsza_ocene(oceny_przedmioty):
    najwyzsza = 0
    for przedmiot, oceny in oceny_przedmioty.items():
        najwyzsza_ocena = max(oceny)
        if najwyzsza_ocena > najwyzsza:
            najwyzsza = najwyzsza_ocena
    return najwyzsza

najlepsza_ocena = znajdz_najwyzsza_ocene(oceny_przedmioty)
print(f"Najlepsza ocena to: {najlepsza_ocena}")