"""
Select the element and put it at the correct index
"""
from typing import List


def selection_sort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def test() -> "Correct Result ♥":
    arrays = [[5,4,3,2,1], [1,2,9,3,4,5,11,0], [7,1,6,8,58,0,2,45,3]]
    for array in arrays:
        print(selection_sort(array))


test()