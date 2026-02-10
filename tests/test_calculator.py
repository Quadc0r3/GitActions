from src import calculator


def test_add_function():
    from calculator import add
    assert add(1, 2) == 3
    assert add(-1, -1) == -2
    assert add(0, 0) == 0
    assert add(100, -50) == 50
    assert add(2.5, 3.5) == 6.0
    assert add(0, 5) == 5
    assert add(-5, 0) == -5
