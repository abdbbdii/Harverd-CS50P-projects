from um import count

def test_time():
    assert count("yum") == 0
    assert count("hi, um") == 1
    assert count("Um") == 1