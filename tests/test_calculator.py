import pytest
from src import calculator


import pytest
from src import calculator

def test_add_positive_integers():
    """Test addition of two positive integers."""
    assert calculator.add(1, 2) == 3
    assert calculator.add(10, 20) == 30
    assert calculator.add(100, 0) == 100

def test_add_negative_integers():
    """Test addition of two negative integers."""
    assert calculator.add(-1, -2) == -3
    assert calculator.add(-10, -20) == -30

def test_add_mixed_integers():
    """Test addition of a positive and a negative integer."""
    assert calculator.add(5, -3) == 2
    assert calculator.add(-3, 5) == 2
    assert calculator.add(-5, 3) == -2
    assert calculator.add(10, -10) == 0

def test_add_zero():
    """Test addition involving zero."""
    assert calculator.add(0, 5) == 5
    assert calculator.add(5, 0) == 5
    assert calculator.add(0, 0) == 0

def test_add_floats():
    """Test addition of floating-point numbers using pytest.approx."""
    assert calculator.add(0.1, 0.2) == pytest.approx(0.3)
    assert calculator.add(1.5, 2.5) == pytest.approx(4.0)
    assert calculator.add(-0.1, 0.1) == pytest.approx(0.0)
    assert calculator.add(-1.23, -4.56) == pytest.approx(-5.79)
    assert calculator.add(10.0, -3.5) == pytest.approx(6.5)

def test_add_large_numbers():
    """Test addition with larger integer values."""
    assert calculator.add(1000000, 2000000) == 3000000
    assert calculator.add(-500000, 1000000) == 500000


import pytest
from src import calculator

def test_sub_function():
    # Test positive integers
    assert calculator.sub(5, 3) == 2
    assert calculator.sub(10, 7) == 3

    # Test with negative integers
    assert calculator.sub(-5, -3) == -2
    assert calculator.sub(-10, -7) == -3

    # Test with mixed positive and negative integers
    assert calculator.sub(5, -3) == 8
    assert calculator.sub(-5, 3) == -8

    # Test with zero
    assert calculator.sub(0, 5) == -5
    assert calculator.sub(5, 0) == 5
    assert calculator.sub(0, 0) == 0

    # Test with floating point numbers, using pytest.approx
    assert calculator.sub(5.5, 2.3) == pytest.approx(3.2)
    assert calculator.sub(10.0, 3.7) == pytest.approx(6.3)
    assert calculator.sub(-2.5, 1.0) == pytest.approx(-3.5)
    assert calculator.sub(0.1, 0.2) == pytest.approx(-0.1)
    assert calculator.sub(1.0, 0.9) == pytest.approx(0.1)

import pytest
from src import calculator

def test_add_functionality():
    # Test positive integers
    assert calculator.add(2, 3) == 5
    assert calculator.add(10, 20) == 30

    # Test negative integers
    assert calculator.add(-2, -3) == -5
    assert calculator.add(-10, -20) == -30

    # Test mixed positive and negative integers
    assert calculator.add(5, -3) == 2
    assert calculator.add(-5, 3) == -2
    assert calculator.add(0, -7) == -7
    assert calculator.add(-7, 0) == -7

    # Test with zero
    assert calculator.add(0, 0) == 0
    assert calculator.add(5, 0) == 5
    assert calculator.add(0, 5) == 5

    # Test floating-point numbers
    assert calculator.add(1.5, 2.5) == pytest.approx(4.0)
    assert calculator.add(0.1, 0.2) == pytest.approx(0.3)
    assert calculator.add(-1.0, 1.0) == pytest.approx(0.0)
    assert calculator.add(10.5, -3.2) == pytest.approx(7.3)

    # Test large numbers
    assert calculator.add(1000000, 2000000) == 3000000
    assert calculator.add(-1000000, 500000) == -500000


import pytest
from src import calculator

def test_sub_positive_integers():
    assert calculator.sub(5, 3) == 2
    assert calculator.sub(10, 7) == 3
    assert calculator.sub(100, 1) == 99

def test_sub_negative_integers():
    assert calculator.sub(-5, -3) == -2
    assert calculator.sub(-3, -5) == 2
    assert calculator.sub(-10, -10) == 0

def test_sub_mixed_integers():
    assert calculator.sub(5, -3) == 8
    assert calculator.sub(-5, 3) == -8
    assert calculator.sub(0, -7) == 7
    assert calculator.sub(-7, 0) == -7

def test_sub_zero():
    assert calculator.sub(0, 0) == 0
    assert calculator.sub(5, 0) == 5
    assert calculator.sub(0, 5) == -5

def test_sub_floats():
    assert calculator.sub(10.5, 3.2) == pytest.approx(7.3)
    assert calculator.sub(3.2, 10.5) == pytest.approx(-7.3)
    assert calculator.sub(0.1, 0.2) == pytest.approx(-0.1)
    assert calculator.sub(1.0, 0.9) == pytest.approx(0.1)
    assert calculator.sub(-1.5, 2.0) == pytest.approx(-3.5)
    assert calculator.sub(2.0, -1.5) == pytest.approx(3.5)
