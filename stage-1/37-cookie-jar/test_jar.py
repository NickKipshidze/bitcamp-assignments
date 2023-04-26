from jar import Jar

def test_init():
    jar = Jar()

    assert jar.capacity == 12

def test_str():
    jar = Jar(capacity = 2048)
    jar.deposit(1024)

    assert str(jar) == jar.cookie*1024

def test_deposit():
    jar = Jar()
    jar.deposit(8)

    assert jar.size == 8

    try:
        jar.deposit(512)
    except ValueError:
        pass
    else:
        assert False

def test_withdraw():
    jar = Jar()
    jar.deposit(4)
    jar.withdraw(2)

    assert jar.size == 2

    try:
        jar.withdraw(16)
    except ValueError:
        pass
    else:
        assert False