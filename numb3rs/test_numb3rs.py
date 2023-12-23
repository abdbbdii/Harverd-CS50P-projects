from numb3rs import validate

def test_true():
    assert validate("123.123.123.123") == True
    assert validate("1.2.3.4") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_false():
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("456.456.456.456") == False
    assert validate("10.20.30.256") == False
