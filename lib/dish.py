class Dish():

    def __init__(self, dish_name, price):
        self.dish_name = dish_name
        self.price = price

    def get_dish_name(self):
        return self.dish_name

    def get_dish_price(self):
        return self.price

    def change_dish_name(self, new_name):
        self.dish_name = new_name

    def change_dish_price(self, new_price):
        self.price = new_price

    def format_dish(self):
        return f'{self.dish_name} - £{self.price}'
