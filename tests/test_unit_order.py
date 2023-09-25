from lib.order import Order
from unittest.mock import Mock
import pytest
from lib.message_sender import TextMessager


"""
Initially oder is empty
throws an error
"""
def test_summary_order_with_empty_order_list():
    order = Order()
    with pytest.raises(Exception) as e:
        order.summary_order()
    err_msg = str(e.value)
    assert err_msg == 'There is no item in your order'

def test_validate_order_with_empty_order_list():
    order = Order()
    customer = Mock()
    with pytest.raises(Exception) as e:
        order.validate_order()
    err_msg = str(e.value)
    assert err_msg == 'There is no item in your order'


"""
Add item to order
"""
def test_add_item_returns_message():
    order = Order()
    dish1 = Mock()
    dish1.get_dish_price.return_value = 25.00
    dish1.get_dish_name.return_value = 'Beef Wellington'
    assert order.add_item(dish1) == 'Beef Wellington added to your order'

"""
Remove item from order
"""
def test_remove_item_returns_message():
    order = Order()
    dish1 = Mock()
    dish1.get_dish_price.return_value = 25.00
    dish1.get_dish_name.return_value = 'Beef Wellington'
    order.add_item(dish1)
    assert order.remove_item(dish1) == 'Beef Wellington removed from your order'


"""
Remove inexistant item from order
"""
def test_remove_inexistant_item_returns_message():
    order = Order()
    dish1 = Mock()
    with pytest.raises(Exception) as e:
        order.remove_item(dish1)
    err_msg = str(e.value)
    assert err_msg == 'This item is not in your order'


'''
Initially there are no items in the order
adds an item and returns summary
'''

def test_adds_item_and_check_summary():
    order = Order()
    item1 = Mock()
    item1.get_dish_price.return_value = 25.00
    item1.get_dish_name.return_value = 'Beef Wellington'
    item2 = Mock()
    item2.get_dish_price.return_value = 15.50
    item2.get_dish_name.return_value = 'Pasta Carbonara'
    order.add_item(item1)
    order.add_item(item2)
    assert order.summary_order() == "1 x Beef Wellington\n1 x Pasta Carbonara\n\nTotal of order: £40.50"


"""
Initially there is an item in the list
removes the item and try to see summary
"""
def test_adds_item_and_remove_one_then_check_summary():
    order = Order()
    item1 = Mock()
    item1.get_dish_price.return_value = 25.00
    item1.get_dish_name.return_value = 'Beef Wellington'
    item2 = Mock()
    item2.get_dish_price.return_value = 15.50
    item2.get_dish_name.return_value = 'Pasta Carbonara'
    order.add_item(item1)
    order.add_item(item2)
    order.remove_item(item1)
    assert order.summary_order() == "1 x Pasta Carbonara\n\nTotal of order: £15.50"

