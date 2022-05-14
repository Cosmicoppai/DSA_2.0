from typing import List


"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n))

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000


Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
"""


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    comb = [None] * (len(nums1) + len(nums2))
    i = 0
    j = 0
    k = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            comb[k] = nums1[i]
            i += 1
        else:
            comb[k] = nums2[j]
            j += 1
        k += 1

    while i < len(nums1):
        comb[k] = nums1[i]
        i += 1
        k += 1
    while j < len(nums2):
        comb[k] = nums2[j]
        j += 1
        k += 1

    n = len(comb)
    if n % 2 != 0:
        return float(comb[n // 2])
    return float(comb[n // 2]+comb[(n - 1) // 2]) / 2.0


"""
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        completed_array = nums1 + nums2
        completed_array.sort()
        
        l = len(completed_array)
        
        if l % 2 == 1:
            return completed_array[int(l/2)]
        
        else:
            i = int(l/2)-1
            return (completed_array[i] + completed_array[i+1]) / 2
"""