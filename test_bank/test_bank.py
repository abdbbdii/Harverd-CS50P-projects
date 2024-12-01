from bank import value

def test_hi():
    assert value("hi bro") == 20
    assert value("Hi bro") == 20

def test_hello():
    assert value("hello ma guy") == 0
    assert value("Hello ma guy") == 0