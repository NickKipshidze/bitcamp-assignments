import bank

def test_value_h():
    assert bank.value("Hi") == 20
    assert bank.value("Hey") == 20
    assert bank.value("Hello") != 20

def test_value_hello():
    assert bank.value("Hi") != 0
    assert bank.value("Hey") != 0
    assert bank.value("Hello") == 0

def test_value_100():
    assert bank.value("Greetings") == 100
    assert bank.value("Gamarjoba") == 100
    assert bank.value("What's up") == 100