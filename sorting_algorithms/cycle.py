from typing import List

"""
Cycle Sort

* When given numbers from range 1,N -> use cyclic sort

==========================================================
* If range is from 0,N then every element will be at index=value
* If range is from 1,N then every element will be at index=value-1

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
E.x:- Find all the numbers Disappeared in the array
"""


def solution(arr: List[int]) -> List[int]:
    i = 0
    while i < len(arr):
        _index = arr[i]-1  # get the correct index
        if arr[_index] == _index+1:  # check if at the correct index the value is present is correct or not
            i += 1
            continue
        arr[i], arr[_index] = arr[_index], arr[i]
    ans = []
    for i in range(len(arr)):
        if i != arr[i]-1:
            ans.append(i+1)

    return ans


"""
Alternate solution:-

my_set = set(arr)
ans - []
for i in range(1, len(arr)+1):
    if i not in my_set:
        ans.append(i)
return ans
"""


print(solution([4, 3, 2, 7, 8, 2, 3, 1]), solution([1,1]))