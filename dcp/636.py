"""Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
"""

from typing import List


def min_ele(arr: List[int], start: int, end: int) -> int:
    if start > end or len(arr) < 1:
        return -1

    if len(arr) == 1 or start == end:
        return arr[0]

    if len(arr) == 2:
        return arr[0] if arr[0] < arr[1] else arr[1]

    while start < end:
        mid = (start + (end-start))//2
        # print(mid, start, end, arr[start:end])
        if arr[mid] > arr[mid+1]:
            return arr[mid+1]
        elif arr[mid-1] < arr[mid]:
            start = mid+1
        else:
            return arr[mid]


if __name__ == "__main__":
    arrays = [[5, 7, 10, 3, 4], [6, 7, 8, 9, 1, 2, 3, 4], [], [2, 3], [1]]
    for _arr in arrays:
        print(min_ele(_arr, 0, len(_arr)))
