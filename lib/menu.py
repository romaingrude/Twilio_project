class Menu():
    
    def __init__(self):
        self._menu = []

    def add_dish_to_menu(self, dish):
        self._menu.append(dish)

    def remove_dish_from_menu(self, dish):
        self._menu.remove(dish)

    def list_menu(self):
        if not self._menu:
            raise Exception('The menu has no dishes')
        return '\n'.join([dish.format_dish() for dish in self._menu])