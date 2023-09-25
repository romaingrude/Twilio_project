from lib.menu import Menu
from unittest.mock import Mock
import pytest

"""
Initially menu has no dishes
"""
def test_no_dishes_in_menu():
    menu = Menu()
    with pytest.raises(Exception) as e:
        menu.list_menu()
    err_msg = str(e.value)
    assert err_msg == 'The menu has no dishes'

"""
Initially the menu has items
lists the menu
"""
def test_adds_dishes_and_returns_menu():
    menu = Menu()
    dish1 = Mock()
    dish2 = Mock()
    dish1.format_dish.return_value = 'Beef Wellington - £24.99'
    dish2.format_dish.return_value = 'Pasta Carbonara - £12.99'
    menu.add_dish_to_menu(dish1)
    menu.add_dish_to_menu(dish2)
    assert menu.list_menu() == 'Beef Wellington - £24.99\nPasta Carbonara - £12.99'

"""
Initially the menu has items, remove item then
lists the menu
"""
def test_adds_dishes_and_removes_one_then_returns_menu():
    menu = Menu()
    dish1 = Mock()
    dish2 = Mock()
    dish1.format_dish.return_value = 'Beef Wellington - £24.99'
    dish2.format_dish.return_value = 'Pasta Carbonara - £12.99'
    menu.add_dish_to_menu(dish1)
    menu.add_dish_to_menu(dish2)
    menu.remove_dish_from_menu(dish1)
    assert menu.list_menu() == 'Pasta Carbonara - £12.99'

