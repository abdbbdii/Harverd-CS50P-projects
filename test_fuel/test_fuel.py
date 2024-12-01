import fuel
import pytest

def test():
    assert fuel.convert("4/5") == 80
    assert fuel.gauge(80) == "80%"
    assert fuel.convert("99/100") == 99
    assert fuel.gauge(99) == "F"
    assert fuel.convert("1/100") == 1
    assert fuel.gauge(1) == "E"
    
    with pytest.raises(ZeroDivisionError):
         fuel.convert('2/0')
    with pytest.raises(ValueError):
         fuel.convert('3/2')
    with pytest.raises(ValueError):
         fuel.convert('cat/dog')