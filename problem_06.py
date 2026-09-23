# Problem 6: Zigzag Conversion
# Difficulty: Medium
#
# Description:
# Given a string s and an integer numRows, arrange the characters
# in a zigzag pattern on the given number of rows and then read
# the characters row by row.
#
# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
# Explanation:
# The string is arranged like this:
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
# Reading row by row gives "PAHNAPLSIIGYIR".
#
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
#
# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"


class Solution:

    def convert(self, s: str, numRows: int) -> str:

        newStr = ''
        rows = []

        if numRows == 1:
            return s

        for i in range(numRows):
            rows.append("")

        current_row = 0
        direction = 1

        for char in s:

            rows[current_row] += char

            if current_row == 0:
                direction = 1

            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        for row in rows:
            newStr += row

        return newStr