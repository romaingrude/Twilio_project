from lib.menu import Menu
from lib.dish import Dish

"""
Add dishes to menu
lists menu
"""
def test_add_dish_and_returns_menu():
    dish1 = Dish('Beef Wellington', 24.99)
    dish2 = Dish('Pasta Carbonara', 12.99)
    menu = Menu()
    menu.add_dish_to_menu(dish1)
    menu.add_dish_to_menu(dish2)
    assert menu.list_menu() == "Beef Wellington - £24.99\nPasta Carbonara - £12.99"

"""
Add dishes to menu
lists menu
"""
def test_add_dish_then_remove_and_returns_menu():
    dish1 = Dish('Beef Wellington', 24.99)
    dish2 = Dish('Pasta Carbonara', 12.99)
    menu = Menu()
    menu.add_dish_to_menu(dish1)
    menu.add_dish_to_menu(dish2)
    menu.remove_dish_from_menu(dish1)
    assert menu.list_menu() == "Pasta Carbonara - £12.99"