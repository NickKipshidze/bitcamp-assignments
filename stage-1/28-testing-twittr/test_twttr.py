import twttr

def test_shorten_lowercase():
    assert twttr.shorten("hello") == "hll"
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("nick") == "nck"

def test_shorten_uppercase():
    assert twttr.shorten("HELLO") == "HLL"
    assert twttr.shorten("TWITTER") == "TWTTR"
    assert twttr.shorten("NICK") == "NCK"

def test_shorten_mixcase():
    assert twttr.shorten("HeLlO") == "HLl"
    assert twttr.shorten("TwItTeR") == "TwtTR"
    assert twttr.shorten("NiCk") == "NCk"