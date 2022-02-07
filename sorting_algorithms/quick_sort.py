"""



"""
from typing import List


def quick_sort(arr: List[int], start: int, end: int) -> List[int]:
    if start >= end:
        return arr
    pi = partition(arr, start, end)
    quick_sort(arr, pi+1, end)
    quick_sort(arr, start, pi-1)
    return arr


def partition(arr: List[int], start: int, end: int) -> int:
    i = start
    pi_elem = arr[end]
    for j in range(start, end):
        if arr[j] <= pi_elem:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1  ## increase the index
    arr[i], arr[end] = arr[end], arr[i]
    return i


if __name__ == "__main__":
    assert quick_sort([5, 4, 3, 2, 1, 0], 0, 5) == [0, 1, 2, 3, 4, 5]
    assert quick_sort([5, 4, 3, 2, 0, -1, -3, 1], 0, 7) == [-3, -1, 0, 1, 2, 3, 4, 5]
    assert quick_sort([1], 0, 0) == [1]
    assert quick_sort([0,4,3,6,2,5],0,5) == [0,2,3,4,5,6]


"""
Time Complexity:- O(N^2) in worst Case and O(NlogN) in average Case
Space Complexity:- O(N)
"""