#!python
from math import floor, ceil

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    '''
    Best time complexity -- O(1), target item is in the first index
    Worst time complexity -- O(n), target item is in the last index
    '''
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    '''
    Best time complexity -- O(1), target item is in the first index
    Worst time complexity -- O(n), target item is in the last index
    '''
    if array[index] == item:
        return index
    elif index == len(array) - 1:
        return None
    else:
        index += 1
        return linear_search_recursive(array, item, index)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)

def binary_search_iterative(array, item):
    # implement binary search iteratively here
    '''
    Best time complexity -- O(1), target item is in the middle index
    Average time complexity -- O(log n), target item is in the last index
    '''
    left = 0
    right = len(array) - 1
    while left <= right:
        mid_index = (right + left) // 2
        arr_mid = array[mid_index]
        if array[mid_index] == item:
            return mid_index
        elif array[mid_index] > item:
            right = mid_index - 1
        else:
            left = mid_index + 1
    return None

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None): # don't pass in list for left and right
    # implement binary search recursively here
    '''
    Best time complexity -- O(1), target item is in the middle index
    Average time complexity -- O(log n), target item is in the last index
    '''
    if left is None and right is None:
        left = 0
        right = len(array) - 1
    if left > right:
        return None
    mid_index = (right + left) // 2
    if array[mid_index] == item:
        return mid_index
    elif array[mid_index] > item:
        return binary_search_recursive(array, item, left, mid_index - 1)
    elif array[mid_index] < item:
        return binary_search_recursive(array, item, mid_index + 1, right)

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
