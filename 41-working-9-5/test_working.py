import working

def test_working_normal():
    assert working.convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert working.convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert working.convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert working.convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

def test_working_errors():
    try:
        working.convert("9:60 AM to 5:60 PM")
        raise AssertionError
    except ValueError:
        pass
    try:
        working.convert("9 AM - 5 PM")
        raise AssertionError
    except ValueError:
        pass
    try:
        working.convert("09:00 AM - 17:00 PM")
        raise AssertionError
    except ValueError:
        pass