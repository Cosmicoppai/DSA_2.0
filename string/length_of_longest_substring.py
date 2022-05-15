"""Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The
answer is "b",
with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s
consists
of
English
letters, digits, symbols and spaces.
"""


def length_of_longest_substring(s: str) -> int:
    if len(s) < 2:
        return len(s)
    if len(s) == 2:
        return 1 if s[0] == s[1] else 2

    start = largest = len_of_substring = i = 0
    store: {str, int} = {}

    for i in range(0, len(s)):
        c = s[i]
        # If we already saw that char , it's position is after our "start point"
        # Means we've encountered
        if (c in store) and (store[c] >= start):

            len_of_substring = i - start  # currentIndex - start_index
            if l > largest:
                largest = l

            start = store[c] + 1

        # Store the last position of the current character
        store[c] = i

    return max((i + 1) - start, largest)
