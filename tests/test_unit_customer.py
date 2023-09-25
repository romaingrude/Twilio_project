from lib.customer import Customer


"""
Initially there is a customer
retrieve their name
"""
def test_get_customer_name():
    customer1 = Customer('Romain Grude', 'Garden Cottage, LA88HF KENDAL', '077628888911')
    assert customer1.get_name() == 'Romain Grude'


"""
Initially there is a customer
retrieve their address
"""
def test_get_customer_address():
    customer1 = Customer('Romain Grude', 'Garden Cottage, LA88HF KENDAL', '077628888911')
    assert customer1.get_address() == 'Garden Cottage, LA88HF KENDAL'


"""
Initially there is a customer
retrieve their phone number
"""
def test_get_customer_phone():
    customer1 = Customer('Romain Grude', 'Garden Cottage, LA88HF KENDAL', '077628888911')
    assert customer1.get_number() == '077628888911'