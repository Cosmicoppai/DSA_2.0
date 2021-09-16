"""
Find a number in RowColMatrix(a matrix which is sorted in row and column)
"""
from typing import List


def RowColMatrix(matrix: List[List[int]], num: int) -> int:
    row, col = 0, len(matrix[0])-1
    while col >= 0 and row <= len(matrix)-1:
        if matrix[row][col] == num:
            return row, col
        if matrix[row][col] > num:
            col -= 1
        else:
            row += 1
    return -1


def test():
    matrix = [
        [1,2,3,4],
        [10,20,30,40],
        [21,25,39,41],
        [26,50, 42, 51]]
    return RowColMatrix(matrix, 25)


# print(test())

"""
Search in a Sorted Matrix
[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
"""


def sorted_matrix(matrix: List[List[int]], target: int) -> int:
    if len(matrix) == 0:
        return -1
    m,n = len(matrix), len(matrix[0])
    left, right = 0, m*n-1
    while left <= right:
        mid = (left+right)//2
        r, c = mid//n, mid % n
        if matrix[r][c] == target:
            return r, c
        if matrix[r][c] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def test_sorted_matrix():
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(sorted_matrix(matrix, 11))


test_sorted_matrix()