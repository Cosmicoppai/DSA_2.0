from typing import List, Optional
from collections import OrderedDict, Counter


"""
Questions Available here: https://leetcode.com/discuss/interview-question/514021/mercari-oa-2020-new-grad
"""

def array_subset(arr: List[int]) -> List[int]:
    arr = sorted(arr)
    freq_dict = OrderedDict()
    arr_sum = sum(arr)

    for ele in arr[::-1]:
        freq_dict[ele] = freq_dict.get(ele, 0) + 1

    a, a_sum, total_sum = [], 0, arr_sum
    for key in freq_dict:
        if freq_dict[key] == 1:
            a.append(key)
            a_sum += key
            total_sum -= key
        if a_sum > total_sum:
            return a[::-1]

    a, a_sum, total_sum = [], 0, arr_sum
    for key in freq_dict:
        a = a + [key] * freq_dict[key]
        sum_of_curr_ele = freq_dict[key] * key
        a_sum += sum_of_curr_ele
        total_sum -= freq_dict[key] * key

        if a_sum > total_sum:
            return a[::-1]


"""
2. Lottery Coupons
"""


def lottery_coupons(coupons: List[int]) -> int:
    coupons_sum: {digit_sum: int, freq_of_tickets: int} = {}
    for coupon in coupons:
        c_sum = number_sum(coupon)
        coupons_sum[c_sum] = coupons_sum.get(c_sum, 0) + 1
    max_winners = max(coupons_sum.values())
    return Counter(coupons_sum.values())[max_winners]


def number_sum(num: int) -> int:
    _sum = 0
    for digit in str(num):
        _sum += int(digit)
    return _sum


"""
3. Compliance Crawler Directory 
"""


def minimum_steps(commands: List[str], curr_dir: Optional[List[str]] = []) -> int:
    execute_command(commands, curr_dir)
    count = 0
    while curr_dir:
        count += 1
        execute_command(["../"], curr_dir)
    return count


def execute_command(commands: List[str], curr_dir: List[str]) -> None:
    for command in commands:
        if command == "./":
            continue
        if command == "../" and curr_dir:
            curr_dir.pop(-1)
            continue
        curr_dir.append(command)


"""
4. Array Game
"""


def count_moves(arr: List[int]) -> int:
    steps = {}

    min_ele = min(arr)

    total_sum = 0

    for ele in arr:
        total_sum += ele

    return total_sum - len(arr)*min_ele


if __name__ == "__main__":
    # print(array_subset([3, 7, 5, 5, 6, 2]))
    # print(array_subset([1, 2, 2, 2, 7]))
    # print(array_subset([1, 2]))
    # print(array_subset([2, 2]))
    # print(lottery_coupons([n for n in range(13)]))
    # print(minimum_steps(commands=["F1/", "F2/", "./", "F3/", "../", "F31/"]))
    print(count_moves([3, 4, 6, 6, 3]))
    print(count_moves([10, 10, 10, 1]))
