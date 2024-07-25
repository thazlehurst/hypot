import pytest
import hypot.source as source


# test sqrt function for input is even
def test_sqrt_even():
    input = 4
    expected_output = 2.0
    output = source.sqrt(input)
    assert output == expected_output


# test sqrt function for input is odd
def test_sqrt_odd():
    input = 9
    expected_output = 3.0
    output = source.sqrt(input)
    assert output == expected_output


# test with zero
def test_sqrt_zero():
    input = 0
    expected_output = 0.0
    output = source.sqrt(input)
    assert output == expected_output


# test with negative number
def test_sqrt_neg():
    input = -4
    expected_output = 2.0
    output = source.sqrt(input)
    assert output == expected_output


# test hypot function
