"""
We consider alphabet with only three letters: "a", "b" and "c". A string is called diverse if no three consecutive letters are the same.
In other words, a diverse string may not contain any of the strings "aaa", “bbb” or “ccc”.

Write a function:

def solution(A, B, C)

that, given three integers A, B and C, returns any longest possible diverse string containing at most A letters ‘a’, at most B letters 'b’
and at most C letters ‘c’. If there is no possibility of building any string, retum empty string.

Example
1. Given A = 6, B = 1 and C = 1, your function may return "aabaacaa”. Note that “aacaabaa" would also be a correct answer. Your
function may return any correct answer.

2. Given A = 1,B = 3 and C = 1 your function may return "abbcb", "bcbab”, "bacbb" or any of several other strings.
3. Given A = 0, B = 1 and C = 8 your function should return “ccbcc", which is the only correct answer in this case.

Assume That

* A,Band C are integers within the range [0..100];
* A+ B+C>0

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

"""

if __name__ == "__main__":

    def solution(A: int, B: int, C: int):

        res = ""

        def add_(nu_: int, chr_: str) -> int:
            nonlocal res
            if not res[-2:] == chr_*2:
                min_ = min(nu_, 2)
                res += chr_*min_
                nu_ -= min_
            return nu_

        while max(A, B, C) > 0:
            if max(A, B, C) == A:
                A = add_(A, "a")
                if max(B, C) == B:
                    B = add_(B, "b")
                else:
                    C = add_(C, "c")

            if max(A, B, C) == B:
                B = add_(B, "b")
                if max(A, C) == A:
                    A = add_(A, "a")
                else:
                    C = add_(C, "c")
            if max(A, B, C) == C:
                C = add_(C, "c")
                if max(B, A) == B:
                    B = add_(B, "b")
                else:
                    A = add_(A, "a")

        print(res)


    solution(6, 1, 1)
    solution(0, 1, 1)
    solution(3, 1, 1)
    solution(66, 66, 66)

