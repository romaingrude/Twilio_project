from lib.order import Order
from lib.dish import Dish
from unittest.mock import Mock, patch
from lib.message_sender import TextMessager
from lib.customer import Customer
from lib.menu import Menu


def test_add_items_to_order_then_summary():
    dish1 = Dish('Penne Arabiata', 12.99)
    dish2 = Dish('Beef Lasagna', 8.99)
    dish3 = Dish('Risotto', 10.99)
    dish4 = Dish('Ciabatta Garlic', 6.99)
    dish5 = Dish('Veal Gnocci', 14.99)
    order = Order()
    order.add_item(dish1)
    order.add_item(dish2)
    order.add_item(dish3)
    order.add_item(dish4)
    order.add_item(dish5)
    assert order.summary_order() == '1 x Penne Arabiata\n1 x Beef Lasagna\n1 x Risotto\n1 x Ciabatta Garlic\n1 x Veal Gnocci\n\nTotal of order: £54.95'


def test_add_items_and_remove_one_then_summary():
    dish1 = Dish('Penne Arabiata', 12.99)
    dish2 = Dish('Beef Lasagna', 8.99)
    dish3 = Dish('Risotto', 10.99)
    dish4 = Dish('Ciabatta Garlic', 6.99)
    dish5 = Dish('Veal Gnocci', 14.99)
    order = Order()
    order.add_item(dish1)
    order.add_item(dish2)
    order.add_item(dish3)
    order.add_item(dish4)
    order.add_item(dish5)
    assert order.summary_order() == '1 x Penne Arabiata\n1 x Beef Lasagna\n1 x Risotto\n1 x Ciabatta Garlic\n1 x Veal Gnocci\n\nTotal of order: £54.95'
    order.remove_item(dish3)
    assert order.summary_order() == '1 x Penne Arabiata\n1 x Beef Lasagna\n1 x Ciabatta Garlic\n1 x Veal Gnocci\n\nTotal of order: £43.96'

# @patch('lib.message_sender.Client')
# def test_send_message_when_validating_order(mock_client):
#     # Create a mock customer
#     customer = Customer('Romain Grude', 'Garden Cottage KENDAL', '07762888911')

#     # Create an instance of Order and add items
#     order = Order()
#     dish1 = Dish('Penne Arabiata', 12.99)
#     dish2 = Dish('Beef Lasagna', 8.99)
#     dish3 = Dish('Risotto', 10.99)
#     dish4 = Dish('Ciabatta Garlic', 6.99)
#     dish5 = Dish('Veal Gnocci', 14.99)
#     order = Order()
#     order.add_item(dish1)
#     order.add_item(dish2)
#     order.add_item(dish3)
#     order.add_item(dish4)
#     order.add_item(dish5)

#     # Create an instance of TextMessager with the mock customer
#     text_messager = TextMessager(customer)

#     # Call the validate_order() method
#     order.validate_order()

#     text_messager.send_message()

#     # Assert that the send_message() method was called on the mock client
#     mock_client.return_value.messages.create.assert_called_once_with(
#         to="+447762888911",
#         from_='+447380314231',
#         body=f"Hi Romain Grude! Your order was placed and will be delivered at 00:42"
#         )

def test_full_integration():
    menu = Menu()
    order = Order()
    customer = Customer('Romain Grude', '123 Main St', '07762888911')
    text_messager = TextMessager(customer)

    # Add dishes to the menu
    dish1 = Dish('Penne Arabiata', 12.99)
    dish2 = Dish('Beef Lasagna', 8.99)
    menu.add_dish_to_menu(dish1)
    menu.add_dish_to_menu(dish2)

    # Add selected dishes to the order
    order.add_item(dish1)
    order.add_item(dish2)

    # Validate the order and send a text message
    order.validate_order()
    text_messager.send_message(order._order, order._total)
