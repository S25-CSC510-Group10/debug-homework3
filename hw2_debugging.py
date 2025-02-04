"""Import the rand file to use randomization process"""
# import rand

def merge_sort(array):
    """Function performing merge sort algorithm"""
    if len(array) == 1:
        return array

    half = len(array)//2

    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))

def recombine(left_arr, right_arr):
    """
    Merges two sorted subarrays into one sorted array.

    :param left_arr: Left sorted subarray
    :param right_arr: Right sorted subarray
    :return: Merged sorted array
    """
    left_index = 0
    right_index = 0
    merge_arr = []

    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            # In case of equality, append the left array element first
            merge_arr.append(right_arr[right_index])
            right_index += 1

    while left_index < len(left_arr):
        merge_arr.append(left_arr[left_index])
        left_index += 1

    while right_index < len(right_arr):
        merge_arr.append(right_arr[right_index])
        right_index += 1

    return merge_arr

def bubble_sort(array):
    """Function performing bubble sort algorithm"""
    n = len(array)

    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n-i-1):

            # Swap if the element found is greater than the next element
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

# arr = rand.random_array([None] * 20)
# arr_out = merge_sort(arr)
# arr_out_bubble = bubble_sort(arr)

# print(arr_out)