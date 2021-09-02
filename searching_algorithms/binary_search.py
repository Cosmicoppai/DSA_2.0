from typing import List

"""
1. Ceiling of a number

Given an array find the ceiling i.e smallest number in the array which is greater than or equal to the given number.

E.x:- [2, 3, 5, 9, 14, 16, 18], target = 15

>>> 16

Solution:-
"""


def find_ceiling(arr: List, target: int):
    if target > arr[len(arr) - 1]:  # if the target exceeds the largest element in the list
        return -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == target:
            return target
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return arr[start]


def test_for_find_ceiling():
    array = [2, 3, 5, 9, 14, 16, 18]
    if find_ceiling(array, 14) == 14 and find_ceiling(array, 15) == 16:
        return "All Test Passed"
    # print(find_ceiling(array, 0, len(array), 14), find_ceiling(array, 0, len(array), 15))
    return "Test Failed"


# print(test_for_find_ceiling())

"""
Find Smallest Letter Greater Than Target
Given a characters array letters that is sorted in non-decreasing order and a character target, return the smallest
character in the array that is larger than the target

E.x:- if target='z' and array = ['a', 'b'] the answer is a
"""


def smallest_letter_greater_than_target(array: List, target: str):
    if target > array[len(array) - 1]:
        return -1
    start, end = 0, len(array)
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == target:
            return target
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return array[start]


def test():
    if smallest_letter_greater_than_target(['c', 'f', 'j'], 'a') == 'c':
        return "Test Passed"
    return "Test Failed"


# print(test())


"""
Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value
If target is not found return array [-1, -1]

E.x:- nums = [5, 7, 7, 8, 8, 10], target = 8
>>> output [3, 4]
"""


def first_and_last_pos(array: List, target: int, find_start_index:bool):
    ans = -1
    if target > array[len(array)-1] or target < array[0]:
        return ans
    start, end = 0, len(array)
    while start <= end:
        mid = start + (end-start)//2
        if array[mid] < target:
            start = mid+1
        elif array[mid] > target:
            end = mid - 1
        else:
            ans = mid
            if find_start_index:
                end = mid - 1
            else:
                start = mid + 1
    return ans


def first_last_pos_test():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    start_index = first_and_last_pos(nums, target, True)
    end_index = first_and_last_pos(nums, target, False)
    assert [start_index, end_index] == [3, 4]


# first_last_pos_test()


"""
Find Position of an element in a sorted array of infinite number

"""


def infinite_array(array: List, start: int, end: int, target: int):
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] < target:
            start = mid + 1
        if array[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1


def test_infinite_array():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 16, 17, 18, 19, 20, 25, 30, 35, 40]
    target = 15
    start, end = 0, 5  # take a chunk of 5 element first and exponentially increase it
    while target > array[end]:
        start = end+1
        end = end * 2
    return infinite_array(array, start, end, target)


print(test_infinite_array())