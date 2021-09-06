from typing import List

"""
Cycle Sort

* When given numbers from range 1,N -> use cyclic sort

"""


def cycle_sort(arr: List[int]) -> List[int]:
    i = 0
    while i < len(arr):
        index_curr_elem = arr[i]-1  # actual index of that element
        if index_curr_elem == i:
            i += 1
            continue
        arr[index_curr_elem], arr[i] = arr[i], arr[index_curr_elem]

    return arr


def test_for_cycle_sort() -> "Correct Result ♥":
    arrays = [[5,4,3,2,1], [1,2,9,5,4,3,6,8,7]]
    for array in arrays:
        print(cycle_sort(array))


# test_for_cycle_sort()


"""

"""