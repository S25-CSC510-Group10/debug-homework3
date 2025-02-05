"""Import the rand file to use randomization process"""

import random


def merge_sort(array):
    """Function performing merge sort algorithm"""
    if len(array) == 1:
        return array

    half = len(array) // 2

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
        for j in range(0, n - i - 1):

            # Swap if the element found is greater than the next element
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

def selection_sort(arr):
    """
    Sorts a list with selection sort.
    :param arr: the list of elements to sort
    :return: a sorted list
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bogosort(list2):
    """
    Sorts a list using the highly inefficient Bogosort algorithm.

    :param array: List of elements to be sorted
    :return: Sorted list
    """
    while is_sorted(list2):
        random.shuffle(list2)
    return list2


def is_sorted(list2):
    """
    Checks if the list is sorted.

    :param array: List to check
    :return: True if sorted, False otherwise
    """
    prev = None
    for x in list2:
        if prev is not None and (prev > x):
            return False
        prev = x
    return True

# arr = rand.random_array([None] * 20)
# arr_out = merge_sort(arr)
# arr_out_bubble = bubble_sort(arr)

# print(arr_out)
