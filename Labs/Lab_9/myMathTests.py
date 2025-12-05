# Zachary Murphy             11-6-25
# Lab #9 Section F

# This code will test multiple functions in the myMath.py file to check that they work as intended.

from myMath import add, subtract, divide, multiply, factorial, sum_of_digits, abs_diff, square_root

def test_add():
    assert add(1, 2) == 3
    assert add(-1, -3) == -4
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(1, 2) == -1
    assert subtract(4, 2) == 2
    assert subtract(0, 0) == 0

def test_divide():
    assert divide(1, 2) == 0.5
    assert divide(9, 0) == "Undefined"
    assert divide(4, 2) == 2

def test_multiply():
    assert multiply(2, 4) == 8
    assert multiply(6, 8) == 48
    assert multiply(0.5, 4) == 2

def test_factorial():
    assert factorial(3) == 6
    assert factorial(5) == 120
    assert factorial(6) == 720

def test_sum_of_digits():
    assert sum_of_digits(100) == 1
    assert sum_of_digits(43830) == 18
    assert sum_of_digits(00000) == 0

def test_abs_diff():
    assert abs_diff(7, 9) == 2
    assert abs_diff(3, 2) == 1
    assert abs_diff(0, 9) == 9

def test_square_root():
    assert square_root(9) == 3
    assert square_root(1) == 1
    assert square_root(49) == 7