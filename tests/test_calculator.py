import pytest
from src import calculator


import pytest
from src import calculator

def test_add_functionality():
    # Test with positive integers
    assert calculator.add(1, 2) == 3
    assert calculator.add(10, 20) == 30
    assert calculator.add(100, 0) == 100

    # Test with negative integers
    assert calculator.add(-1, -2) == -3
    assert calculator.add(-10, -5) == -15
    assert calculator.add(-5, 0) == -5

    # Test with mixed positive and negative integers
    assert calculator.add(5, -3) == 2
    assert calculator.add(-7, 2) == -5
    assert calculator.add(0, 0) == 0

    # Test with floating-point numbers, using pytest.approx for precision
    assert calculator.add(0.1, 0.2) == pytest.approx(0.3)
    assert calculator.add(1.5, 2.5) == pytest.approx(4.0)
    assert calculator.add(-0.5, 1.0) == pytest.approx(0.5)
    assert calculator.add(3.14159, 2.71828) == pytest.approx(5.85987)

    # Test with large numbers
    assert calculator.add(1_000_000, 2_000_000) == 3_000_000
    assert calculator.add(-1_000_000, 500_000) == -500_000
