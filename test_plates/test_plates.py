from plates import is_valid

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("NRVOUS") == True

def test_invalid():
    assert is_valid("CS05") == False
    assert is_valid("CS50P2") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("12345") == False