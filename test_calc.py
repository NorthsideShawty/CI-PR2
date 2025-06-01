from calc import add 

def test_add():
    assert add(2, 7) == 9
    assert add(-70, 1) == -69
    assert add(123, -123) == 0