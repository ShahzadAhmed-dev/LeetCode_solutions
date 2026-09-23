# Problem 7: Reverse Integer
# Difficulty: Medium
#
# Description:
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit
# integer range, return 0.
#
# The signed 32-bit integer range is:
# -2147483648 to 2147483647
#
# Example 1:
# Input: x = 123
# Output: 321
#
# Example 2:
# Input: x = -123
# Output: -321
#
# Example 3:
# Input: x = 120
# Output: 21


class Solution:

    def reverse(self, x: int) -> int:

        negative = x < 0
        x = abs(x)

        reverse = 0

        while x != 0:

            last_digit = x % 10
            reverse = reverse * 10 + last_digit
            x = x // 10

        if negative:
            reverse = -reverse

        if reverse < -2147483648 or reverse > 2147483647:
            return 0

        return reverse