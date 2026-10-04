def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Integration function
def calculate(a, b):
    result = {
        "sum": add(a, b),
        "difference": subtract(a, b),
        "product": multiply(a, b),
        "quotient": divide(a, b)
    }

    return result


# ============================================================
# TEST CODE: test_calculator.py
# ============================================================

import pytest
from hypothesis import given, strategies as st


# ---------------- UNIT TESTS ----------------

def test_add():
    assert add(10, 5) == 15


def test_subtract():
    assert subtract(10, 5) == 5


def test_multiply():
    assert multiply(10, 5) == 50


def test_divide():
    assert divide(10, 5) == 2


# ---------------- EXCEPTION TEST ----------------

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


# ---------------- INTEGRATION TEST ----------------

def test_calculate():
    result = calculate(10, 5)

    assert result["sum"] == 15
    assert result["difference"] == 5
    assert result["product"] == 50
    assert result["quotient"] == 2


# ============================================================
# HYPOTHESIS PROPERTY-BASED TESTS
# ============================================================

@given(st.integers(), st.integers())
def test_add_property(a, b):
    assert add(a, b) == b + a


@given(st.integers(), st.integers())
def test_multiply_property(a, b):
    assert multiply(a, b) == b * a


@given(st.integers(), st.integers())
def test_subtract_property(a, b):
    assert subtract(a, b) + b == a


@given(
    st.integers(),
    st.integers().filter(lambda x: x != 0)
)
def test_divide_property(a, b):
    assert divide(a, b) * b == a


print(calculate(10, 5))