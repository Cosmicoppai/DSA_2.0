"""
Pattern Questions
"""

"""
How to Approach :- 1. Run the outer for loop the number of times we're having the line.
2. Identify for every row no, how many columns are there or type of elements in the column.
"""


"""
1.  *****
    *****
    *****
    *****
    *****
"""


def ques_1(n):
    for i in range(n):
        for j in range(n):
            print('★', end="")
        print("")


"""
2.  *
    **
    ***
    ****
    *****
"""


def ques_2(n):
    for i in range(1, n+1):
        for j in range(i):
            print('★', end="")
        print("")


"""
3.  *****
    ****
    ***
    **
    *
"""


def ques_3(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print('★', end="")
        print("")


"""
4.  *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
"""


def ques_4(n):
    for i in range(1, n//2+1):
        for j in range(i):
            print('★', end="")
        print("")
    for i in range(n-(n//2), 0, -1):
        for j in range(i):
            print('★', end="")
        print("")



"""
5.      *
       ***
      *****
     *******
    *********

"""


def ques_5(n):
    k = n
    for i in range(n):
        for j in range(k):
            print(end=" ")
        k -= 1
        for j in range(i):
            print('★ ', end="")
        print("\r")



"""
7 .      *
        * *
       * * *
      * * * *
     * * * * *
      * * * *
       * * *
        * *
         *


"""


def ques_7(n):
    k = n  # no of spaces in a particular row
    for i in range(2*n):
        for j in range(abs(k)):
            print(" ", end="")
        k -= 1
        for j in range(i if i < n else 2*n-i):  # if i is greater then n than no. of pattern element equal to 2*n-1
            print('★ ', end="")
        print("\r")



if __name__ == "__main__":
    ques_1(5)
    ques_2(5)
    ques_3(5)
    ques_4(5)
    ques_5(5)
    ques_7(7)