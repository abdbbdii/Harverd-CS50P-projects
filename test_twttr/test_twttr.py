from twttr import shorten

def test_small():
    assert shorten("twitter") == "twttr"

def test_capital():
    assert shorten("TWITTER") == "TWTTR"

def test_number():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("!@#$%") == "!@#$%"