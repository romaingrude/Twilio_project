import tkinter as tk
import os
import sys
import time

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the Python module search path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Import the modules
from lib.order import Order
from lib.menu import Menu
from lib.dish import Dish
from lib.customer import Customer
from lib.message_sender import TextMessager

# Create instances of the classes
menu = Menu()
order = Order()
customer = Customer('Romain Grude', '123 Main St', '07762888911')
text_messager = TextMessager(customer)

# Add dishes to the menu
dish1 = Dish('Penne Arabiata', 12.99)
dish2 = Dish('Beef Lasagna', 8.99)
dish3 = Dish('Margherita Pizza', 10.99)
dish4 = Dish('Chicken Alfredo', 14.99)
dish5 = Dish('Caesar Salad', 6.99)
dish6 = Dish('French Toast', 7.99)
dish7 = Dish('Italian Gelato', 4.99)
dish8 = Dish('Rhum Crepes', 8.99)

menu.add_dish_to_menu(dish1)
menu.add_dish_to_menu(dish2)
menu.add_dish_to_menu(dish3)
menu.add_dish_to_menu(dish4)
menu.add_dish_to_menu(dish5)
menu.add_dish_to_menu(dish6)
menu.add_dish_to_menu(dish7)
menu.add_dish_to_menu(dish8)

# Tkinter GUI
root = tk.Tk()
root.title("Order System")

# Function to handle adding items to the order
def add_to_order():
    selected_dish_index = menu_listbox.curselection()
    if selected_dish_index:
        selected_dish_index = selected_dish_index[0]
        selected_dish_info = menu_listbox.get(selected_dish_index)
        selected_dish_name = selected_dish_info.split(' - ')[0]  # Extract the dish name

        selected_dish = None
        for dish in menu._menu:
            if dish.get_dish_name() == selected_dish_name:
                selected_dish = dish
                break

        if selected_dish:
            order_message = order.add_item(selected_dish)
            order_summary_text.set(order_message)
            update_order_list()
            update_total_amount()

# Function to handle removing items from the order
def remove_from_order():
    selected_order_index = order_list.curselection()
    if selected_order_index:
        selected_order_index = selected_order_index[0]
        removed_item_name = order_list.get(selected_order_index)
        for item in order._order:
            if item.get_dish_name() == removed_item_name:
                message = order.remove_item(item)  # Get the message from remove_item
                update_order_list()
                update_total_amount()
                order_summary_text.set(message)


# Function to update the order list
def update_order_list():
    order_list.delete(0, tk.END)
    for item in order._order:
        order_list.insert(tk.END, item.get_dish_name())

# Function to update the total amount
def update_total_amount():
    total_amount.set(f"Total Amount Due: £{order._total:.2f}")

# Function to handle validating the order
def validate_order():
    try:
        order.validate_order()
        total_amount_paid = order._total  # Get the total amount paid
        text_messager.send_message(order._order, total_amount_paid)  # Pass the list of items and total amount
        order_summary_text.set("Order validated. Thank you!")
        update_order_list()
        update_total_amount()
        # Close the window 3 seconds after clicking "Validate Order"
        root.after(3000, root.destroy)
    except Exception as e:
        order_summary_text.set(str(e))

# Menu Listbox
menu_listbox = tk.Listbox(root)
menu_listbox.pack()

# Populate the menu listbox with dishes and prices
for dish in menu.list_menu().split('\n'):
    menu_listbox.insert(tk.END, dish)

# Order Summary Label
order_summary_text = tk.StringVar()
order_summary_label = tk.Label(root, textvariable=order_summary_text)
order_summary_label.pack()

# Order Listbox
order_list = tk.Listbox(root)
order_list.pack()

# Total Amount Label
total_amount = tk.StringVar()
total_amount_label = tk.Label(root, textvariable=total_amount)
total_amount_label.pack()

# Add to Order Button
add_to_order_button = tk.Button(root, text="Add to Order", command=add_to_order)
add_to_order_button.pack()

# Remove from Order Button
remove_from_order_button = tk.Button(root, text="Remove from Order", command=remove_from_order)
remove_from_order_button.pack()

# Validate Order Button
validate_order_button = tk.Button(root, text="Validate Order", command=validate_order)
validate_order_button.pack()

root.mainloop()
