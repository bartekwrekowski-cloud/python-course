from Shop.apple import Apple
from Shop.order import Order
from Shop.potato import Potato

def run_execute():
    green_apple = Apple("green","L",10)
    red_apple = Apple("red","M",15)
    # print(green_apple.species_name, green_apple)
    # print(red_apple.species_name, red_apple)

    old_potato = Potato("sweet","L",30)
    # print(old_potato.species_name, old_potato)

    first_order = Order.random_order()
    first_order.show_order()
    
    print(f"Cena za zielone jabłka: ", green_apple.calculate_total_price(10))
    print(f"Cena za czerwona jabłka: ",  red_apple.calculate_total_price(15))
    print(f"Cena za ziemniaki: " , old_potato.calculate_total_price(20))

if __name__ == '__main__':
    run_execute()
