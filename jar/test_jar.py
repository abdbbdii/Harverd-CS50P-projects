from jar import Jar
import pytest


def test_init():
    jar = Jar(13)
    assert jar.capacity == 13


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError):
        jar.deposit(12)


def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(4)
    assert str(jar) == "🍪"
    with pytest.raises(ValueError):
        jar.withdraw(2)