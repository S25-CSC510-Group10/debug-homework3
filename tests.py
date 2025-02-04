"""Used to randomize test arrays"""
import random
import hw2_debugging


def test_merge_sort_1():
    """Test merge sort in first instance"""
    # Create correct and incorrect arrays
    test_arr = [5, 7, 3, 6, 4, 2, 1, 8]
    compare_arr = [1, 2, 3, 4, 5, 6, 7, 8]

    # Compare and assert correct functionality
    assert compare_arr == hw2_debugging.merge_sort(test_arr)


def test_merge_sort_2():
    """Test merge sort in second instance"""
    # Create correct and incorrect arrays
    test_arr = [8, 7, 6, 5, 4, 3, 2, 1]
    compare_arr = [1, 2, 3, 4, 5, 6, 7, 8]

    # Compare and assert correct functionality
    assert compare_arr == hw2_debugging.merge_sort(test_arr)


def test_merge_sort_3():
    """Test merge sort in third instance"""
    # Create correct and incorrect arrays
    test_arr = [34, 5, 1, 13, 55, 2, 3, 1, 21, 8]
    compare_arr = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    # Compare and assert correct functionality
    assert compare_arr == hw2_debugging.merge_sort(test_arr)


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


def test_merge_sort_6():
    """
    Testing mergesort with a very large array of binary numbers.
    """
    array_size = 10000
    arr_large = [random.randint(0, 1) for _ in range(array_size)]
    arr_expected = sorted(arr_large)
    arr_sorted = hw2_debugging.merge_sort(arr_large)

    assert arr_sorted == arr_expected

def test_merge_sort_7():
    """Test merge sort with a trivial example"""
    # Create static and manipulated arrays
    test_arr = [5,7,3,6,4,2,1,8]
    compare_arr = [1,2,3,4,5,6,7,8]
    assert compare_arr == hw2_debugging.merge_sort(test_arr)

def test_merge_sort_8():
    """ Test with negative and positive numbers."""
    # Create static and manipulated arrays
    test_arr = [-1,7,0,6,3,2,1,8]
    compare_arr = [-1,0,1,2,3,6,7,8]
    assert compare_arr == hw2_debugging.merge_sort(test_arr)

def test_merge_sort_9():
    """ Test with only negative numbers."""
    # Create static and manipulated arrays
    test_arr = [-8,-7,-4,-6,-3,-2,0,-1]
    compare_arr = [-8,-7,-6,-4,-3,-2,-1,0]
    # Compare and assert correct functionality
    assert compare_arr == hw2_debugging.merge_sort(test_arr)
