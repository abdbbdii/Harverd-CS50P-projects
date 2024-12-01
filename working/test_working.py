from working import convert
import pytest


def test_time():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_error():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
