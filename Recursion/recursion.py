"""When a function calls itself and exits on the base condition"""
from typing import List

"""
E.x:- Find the nth fibonacci number

"""


def fibonacci_number(n: int) -> int:
    if n <= 2:
        return 1
    return fibonacci_number(n-1) + fibonacci_number(n-2)
    # return (((1+(5**0.5))/2)**n)/(5**0.5)  -> Formula for Fibonacci Number


def test_fibonacci_number():
    print(fibonacci_number(5))
    print(fibonacci_number(0))
    # print(fibonacci_number(100))
    print(fibonacci_number(10))


"""
Binary Search with Recursion
"""


def bs_recursion(arr: List, start: int, end: int, num: int) -> int:
    if start > end:
        return -1
    mid = start + (end-start)//2
    if arr[mid] == num:
        return mid
    if arr[mid] > num:
        return bs_recursion(arr,start, mid-1, num)
    return bs_recursion(arr,mid+1, end, num)


def test_bs_recursion():
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(bs_recursion(arr,0, len(arr), 3))
    print(bs_recursion([100, 200, 400, 401, 405, 410, 415],0,7, 415))



"""

"""
# test_bs_recursion()
# test_fibonacci_number()