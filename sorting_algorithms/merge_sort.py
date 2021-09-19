"""
It's a divide and conquer Algorithm.

MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:
             middle m = l+ (r-l)/2
     2. Call mergeSort for first half:
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)
"""
from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2

    L = arr[:mid]  # SORT THE FIRST HALF
    R = arr[mid:]  # Sort the Second Half
    merge_sort(L)
    merge_sort(R)

    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    arr2 = [1, 2, 3, 4, -8, 0, 5, 6, 1]
    arr3 = [1]
    merge_sort(arr1)
    merge_sort(arr2)
    assert arr1 == [0, 1,2, 3, 4, 5, 6, 7, 8, 9]
    assert arr2 == [-8, 0, 1, 1, 2, 3, 4, 5, 6]
    assert arr3 == [1]

"""
Time Complexity:- O(NlogN)
Space Complexity:- O(N)
"""