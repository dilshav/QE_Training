# Calculator Test
# Activity 21
# Using pytest:
# Create a new test file and write test to validate the following cases:
# Sum of two numbers
# Difference of two numbers
# Product of two numbers
# Quotient of two numbers
# Subsets
# Activity 22
# Using pytest:
# In the same file as the previous activity, do the following:
# Apply the marker 'activity' to the last 2 test methods.
# Run tests based on substring
# Run tests based using the 'activity' marker.

import pytest

def test_sum():
    num1=5
    num2=10
    assert num1+num2 ==15

def test_diff():
    num1=33
    num2=12
    assert num1-num2 == 21

@pytest.mark.activity
def test_prod():
    num1=5
    num2=2
    assert num1*num2 == 10

@pytest.mark.activity
def test_quot():
    num1=10
    num2=2
    assert num1/num2 == 5















