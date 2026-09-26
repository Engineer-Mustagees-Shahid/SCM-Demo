from calculator import calculate_discount

def test_regular_customer():
    assert calculate_discount(100, False) == 15

def test_member_custumer():
    assert calculate_discount(100, True) == 20
