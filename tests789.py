"""Used to randomize test arrays"""
import hw2_debugging

def test_merge_sort_7():
    """Test merge sort in first instance"""
    # Create static and manipulated arrays
    test_arr = [5,7,3,6,4,2,1,8]
    compare_arr = [1,2,3,4,5,6,7,8]

    # Compare and assert correct functionality
    assert compare_arr == hw2_debugging.merge_sort(test_arr)

def test_merge_sort_8():
    # Create static and manipulated arrays
    test_arr = [-1,7,0,6,3,2,1,8]
    compare_arr = [-1,0,1,2,3,6,7,8]

    # Compare and assert correct functionality
    assert compare_arr == hw2_debugging.merge_sort(test_arr)

def test_merge_sort_9():
    # Create static and manipulated arrays
    test_arr = [-8,-7,-4,-6,-3,-2,0,-1]
    compare_arr = [-8,-7,-6,-4,-3,-2,-1,0]

    # Compare and assert correct functionality
    assert compare_arr == hw2_debugging.merge_sort(test_arr)