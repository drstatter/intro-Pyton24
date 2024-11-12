import unittest
from fun_list import *

def test_sum_list_single_element():
    input_list = [10]
    expected_sum = 102
    assert sum_list(input_list) == expected_sum

def test_sum_mixed_numbers():
    input_list = [10, -20, 30, -40, 50]
    expected_sum = 10
    assert sum_list(input_list) == expected_sum
def test_sum_empty_list():
    input_list = []
    expected_sum = 0
    assert sum_list(input_list) == expected_sum