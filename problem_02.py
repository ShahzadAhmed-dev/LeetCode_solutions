# Problem 2: Add Two Numbers
# Difficulty: Medium
#
# Description:
# Given two non-empty linked lists representing two non-negative integers,
# add the two numbers and return the sum as a linked list.
# The digits are stored in reverse order.
#
# Example 1:
# Input: l1 = [2, 4, 3], l2 = [5, 6, 4]
# Output: [7, 0, 8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [9, 9, 9], l2 = [1]
# Output: [0, 0, 0, 1]
# Explanation: 999 + 1 = 1000.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
           if l1:
               x = l1.val
           else:
               x = 0

           if l2:
               y = l2.val
           else:
               y = 0

           number = x + y + carry           
           digit = number % 10
           carry = number // 10
           if l1:
               l1 = l1.next
           if l2:
               l2 = l2.next
           current.next = ListNode(digit)
           current = current.next
        return dummy.next