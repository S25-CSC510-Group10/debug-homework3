"""Used to randomize test arrays"""
import rand
import hw2_debugging

def test_merge_sort_1():
    """Test merge sort in first instance"""
    # Create static and manipulated arrays
    test_arr = [5,7,3,6,4,2,1,8]
    compare_arr = [1,2,3,4,5,6,7,8]

    # Compare and assert correct functionality
    assert compare_arr == hw2_debugging.merge_sort(test_arr)
