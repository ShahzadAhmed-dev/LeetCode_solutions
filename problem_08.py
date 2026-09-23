# Problem 8: String to Integer (atoi)
# Difficulty: Medium
#
# Description:
# Implement the myAtoi(string s) function, which converts a string
# into a 32-bit signed integer.
#
# The function should:
# 1. Ignore leading whitespace.
# 2. Check for an optional '+' or '-' sign.
# 3. Read digits until a non-digit character is found.
# 4. Convert the digits into an integer.
# 5. Clamp the result to the 32-bit signed integer range.
#
# The signed 32-bit integer range is:
# -2147483648 to 2147483647
#
# Example 1:
# Input: s = "42"
# Output: 42
#
# Example 2:
# Input: s = "   -42"
# Output: -42
#
# Example 3:
# Input: s = "4193 with words"
# Output: 4193
#
# Example 4:
# Input: s = "words and 987"
# Output: 0
#
# Example 5:
# Input: s = "-91283472332"
# Output: -2147483648


class Solution:

    def myAtoi(self, s: str) -> int:

        s = s.lstrip()

        if not s:
            return 0

        sign = 1

        if s[0] == '-':
            sign = -1

        elif s[0] == '+':
            sign = 1

        i = 0

        if s[0] == '-' or s[0] == '+':
            i = 1

        num = 0

        while i < len(s) and s[i].isdigit():

            num = num * 10 + int(s[i])
            i += 1

        num = num * sign

        if num < -2147483648:
            return -2147483648

        if num > 2147483647:
            return 2147483647

        return num