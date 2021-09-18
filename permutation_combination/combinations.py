from typing import List
"""
例：－ Given Two integers n and k, return all possible combinations k numbers out of the range [1, n]
"""


def combination(n: int, k: int) -> List[List[int]]:
    res = []

    def backtrack(start: int, comb: List):
        if len(comb) == k:
            res.append(comb.copy())
            return
        for i in range(start, n+1):
            comb.append(i)
            backtrack(i+1, comb)
            comb.pop()
    backtrack(1, [])
    return res




if __name__ == "__main__":
    print(combination(4, 2))
    print(combination(1, 1))
    print(combination(5, 3))