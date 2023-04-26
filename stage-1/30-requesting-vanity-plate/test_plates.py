import plates

def test_valid():
    assert plates.is_valid("AAA459") == True
    assert plates.is_valid("AA") == True
    assert plates.is_valid("BQ32") == True

def test_invalid_zero():
    assert plates.is_valid("BB023") == False
    assert plates.is_valid("OP057") == False
    assert plates.is_valid("GLS043") == False

def test_invalid_middle_nums():
    assert plates.is_valid("BDSA34DS") == False
    assert plates.is_valid("TE43DW") == False
    assert plates.is_valid("LS32LS") == False

def test_invalid_legth():
    assert plates.is_valid("A") == False
    assert plates.is_valid("AAABBBCCC") == False
    assert plates.is_valid("AA223344") == False