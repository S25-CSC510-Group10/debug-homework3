"""Used to randomize test arrays"""
import hw2_debugging

def test_merge_sort_1():
    """Test merge sort in first instance"""
    # Create correct and incorrect arrays
    test_arr = [5,7,3,6,4,2,1,8]
    compare_arr = [1,2,3,4,5,6,7,8]

    # Compare and assert correct functionality
    assert compare_arr == hw2_debugging.merge_sort(test_arr)

def test_merge_sort_2():
    """Test merge sort in second instance"""
    # Create correct and incorrect arrays
    test_arr = [8,7,6,5,4,3,2,1]
    compare_arr = [1,2,3,4,5,6,7,8]

    # Compare and assert correct functionality
    assert compare_arr == hw2_debugging.merge_sort(test_arr)

def test_merge_sort_3():
    """Test merge sort in third instance"""
    # Create correct and incorrect arrays
    test_arr = [34,5,1,13,55,2,3,1,21,8]
    compare_arr = [1,1,2,3,5,8,13,21,34,55]

    # Compare and assert correct functionality
    assert compare_arr == hw2_debugging.merge_sort(test_arr)
