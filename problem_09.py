# Problem 9: Palindrome Number
# Difficulty: Easy
#
# Description:
# Given an integer x, return True if x is a palindrome,
# and False otherwise.
#
# A palindrome number reads the same forward and backward.
#
# Example 1:
# Input: x = 121
# Output: True
# Explanation: 121 reads the same forward and backward.
#
# Example 2:
# Input: x = -121
# Output: False
# Explanation: From left to right it reads -121,
# but from right to left it reads 121-.
#
# Example 3:
# Input: x = 10
# Output: False
# Explanation: 10 reads as 01 when reversed.


class Solution:

    def isPalindrome(self, x: int) -> bool:

        original = x
        reverse = 0

        while x > 0:

            last_num = x % 10
            reverse = reverse * 10 + last_num
            x = x // 10

        if original == reverse:
            return True
        else:
            return False