from typing import Optional


"""
Problem Statement:- https://leetcode.com/problems/add-two-numbers/
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    num1 = str(l1.val)
    num2 = str(l2.val)

    while l1.next:
        l1 = l1.next
        num1 += str(l1.val)

    while l2.next:
        l2 = l2.next
        num2 += str(l2.val)

    ans = str(int(num1[::-1]) + int(num2[::-1]))[::-1]

    head = ListNode(ans[0])
    temp = head
    for i in range(1, len(ans)):
        temp.next = ListNode(ans[i])
        temp = temp.next

    return head