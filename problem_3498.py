# Problem 3527: Find the Most Common Response
# Difficulty: Easy
#
# Description:
# Given a string s, calculate its reverse degree.
#
# The reverse alphabet position of a lowercase letter is:
# a = 26, b = 25, c = 24, ..., z = 1.
#
# For each character, multiply its reverse alphabet position
# by its position in the string (starting from 1), then return
# the sum of all these values.
#
# Example 1:
# Input: s = "abc"
# Output: 148
#
# Explanation:
# a = 26 × 1 = 26
# b = 25 × 2 = 50
# c = 24 × 3 = 72
#
# 26 + 50 + 72 = 148


class Solution:

    def reverseDegree(self, s: str) -> int:

        result = 0

        for i, ch in enumerate(s):

            position = i + 1
            alphabet_position = ord(ch) - 96
            reverse_position = 27 - alphabet_position

            result += reverse_position * position

        return result