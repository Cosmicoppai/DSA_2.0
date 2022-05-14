"""
Design an algorithm and write code to remove the duplicate characters in a string
without using any additional buffer NOTE: One or two additional variables are fine
An extra copy of the array is not
"""
from typing import List


def remove_duplicate(string: List[str]) -> List[str]:
    duplicates = 0

    if string is None:
        return string

    if len(string) < 2:
        return string

    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == 0:
                continue
            if string[i] == string[j]:
                duplicates += 1
                string[j] = 0
    for _ in range(duplicates):
        string.remove(0)
    return string


if __name__ == "__main__":
    print(remove_duplicate(["a", "b", "c", "a", "b", "c", "d"]))
