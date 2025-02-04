"""Used to randomize test arrays"""

import hw2_debugging
import random
import sys


def test_merge_sort_4():
    """
    Testing mergesort with a small array
    """
    arr_small = [5, 1, 3, 6]
    arr_sorted = hw2_debugging.merge_sort(arr_small)
    arr_expected = [1, 3, 5, 6]

    assert arr_sorted == arr_expected


def test_merge_sort_5():
    """
    Testing mergesort with a small array containing duplicates
    """

    arr_small = [6, 5, 5, 6]
    arr_sorted = hw2_debugging.merge_sort(arr_small)
    arr_expected = [5, 5, 6, 6]

    assert arr_sorted == arr_expected


import random
import sys


def test_merge_sort_6():
    """
    Testing mergesort with a very large array of binary numbers.
    """
    array_size = 10000
    arr_large = [random.randint(0, 1) for _ in range(array_size)]
    arr_expected = sorted(arr_large)
    arr_sorted = hw2_debugging.merge_sort(arr_large)

    assert arr_sorted == arr_expected
