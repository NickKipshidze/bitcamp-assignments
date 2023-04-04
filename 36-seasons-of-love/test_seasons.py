import seasons

def test_minutes_to_text():
    assert seasons.minutes_to_text(64) == "sixty-four minutes"
    assert seasons.minutes_to_text(1024) == "one thousand and twenty-four minutes"
    assert seasons.minutes_to_text(2048) == "two thousand and forty-eight minutes"