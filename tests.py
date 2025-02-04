"""Used to test merge sort"""
import hw2_debugging

"""Used to randomize test arrays"""
import rand

def test_merge_sort_1():
    """Test merge sort in first instance"""
    # Create static and manipulated arrays
    test_arr = [1,2,3,4,5,6,7,8]
    compare_arr = test_arr

    # Compare and assert correct functionality
    assert compare_arr == hw2_debugging.merge_sort(rand.random_array(test_arr))
