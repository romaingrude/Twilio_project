class Order():

    def __init__(self):
        self._order = []
        self._total = 0

    def add_item(self, item):
        self._order.append(item)
        self._total += item.get_dish_price()
        return f'{item.get_dish_name()} added to your order'

    def remove_item(self, item):
        if item not in self._order:
            raise Exception('This item is not in your order')
        else:
            self._order.remove(item)
            self._total -= item.get_dish_price()
            return f'{item.get_dish_name()} removed from your order'
        
    def summary_order(self):
        if not self._order:
            raise Exception('There is no item in your order')
        else:
            summary = ""
            for item in self._order:
                count = self._order.count(item)
                summary += f"{count} x {item.get_dish_name()}\n"
            total_rounded = round(self._total, 2)
            return f"{summary}\nTotal of order: £{total_rounded:.2f}"

    def validate_order(self):
        if not self._order:
            raise Exception('There is no item in your order')