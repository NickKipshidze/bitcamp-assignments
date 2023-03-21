import fuel

def test_gauge():
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"

def test_convert():
    assert fuel.convert("100/100") == 100
    assert fuel.convert("50/100") == 50
    assert fuel.convert("1032/5032") == 20