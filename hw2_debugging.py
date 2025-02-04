import rand

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
    """
    Recursively sorts an array using Merge Sort.
    :param array: List of elements to be sorted
    :return: Sorted list
    """
    
    if len(arr) == 1:
        return arr

    half = len(arr) // 2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


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
            merge_arr.append(right_arr[right_index])
            right_index += 1

    while left_index < len(left_arr):
        merge_arr.append(left_arr[left_index])
        left_index += 1

    while right_index < len(right_arr):
        merge_arr.append(right_arr[right_index])
        right_index += 1

    return merge_arr

arr = rand.random_array([None] * 20)
arr_out_selection = selection_sort(arr)
arr_out = merge_sort(arr)

print(arr_out)
