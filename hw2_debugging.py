"""
Module for using mergesort and bogosort
"""

import rand
import random


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
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr


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


arr1 = rand.random_array([None] * 20)
arr_out = merge_sort(arr1)
arr_bogo = bogosort(arr1)
print(arr_out)
