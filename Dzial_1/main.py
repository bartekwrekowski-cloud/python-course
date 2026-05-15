import math

import hello_world

oceny_przedmioty = {
    "Matematyka": [5,3,5,4],
    "Angielski": [5,3,5,4],
    "Historia": [5,3,5,4]
}

najlepsza_ocena = hello_world.znajdz_najwyzsza_ocene(oceny_przedmioty)
print(f"Najlepsza ocena to: {najlepsza_ocena}")

sinus_180 = math.sin(math.pi)

print(f"sinus 100 to: {sinus_180}")

very_big_number = 100000000000
the_biggest_number = math.inf

print('the_biggest_number > very_big_number:', the_biggest_number>very_big_number)

