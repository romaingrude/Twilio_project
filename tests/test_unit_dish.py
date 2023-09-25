from lib.dish import Dish

"""
Adding a dish
returns its name
"""
def test_get_dish_name():
    dish1 = Dish('Beef Wellington', 24.99)
    assert dish1.get_dish_name() == 'Beef Wellington'


"""
Adding a dish
returns its price
"""
def test_get_dish_price():
    dish1 = Dish('Beef Wellington', 24.99)
    assert dish1.get_dish_price() == 24.99


"""
Initially there is a dish
replace its name
"""
def test_replace_dish_name():
    dish1 = Dish('Beef Wellington', 24.99)
    dish1.change_dish_name('Pasta al arabiata')
    assert dish1.get_dish_name() == 'Pasta al arabiata'


"""
Initially there is a dish
replace its price
"""
def test_replace_dish_price():
    dish1 = Dish('Beef Wellington', 24.99)
    dish1.change_dish_price(20.99)
    assert dish1.get_dish_price() == 20.99

"""
Initially there is a dish
format the output
"""
def test_format_dish_name():
    dish1 = Dish('Beef Wellington', 24.99)
    assert dish1.format_dish() == 'Beef Wellington - £24.99'




