# Problem 10: Regular Expression Matching
# Difficulty: Hard
#
# Description:
# Given an input string s and a pattern p, implement regular
# expression matching with support for:
#
# '.' → Matches any single character.
# '*' → Matches zero or more of the preceding element.
#
# The entire string must match the pattern.
#
# Example 1:
# Input: s = "aa", p = "a"
# Output: False
# Explanation: "a" does not match the entire string "aa".
#
# Example 2:
# Input: s = "aa", p = "a*"
# Output: True
# Explanation: '*' means zero or more occurrences of 'a'.
#
# Example 3:
# Input: s = "ab", p = ".*"
# Output: True
# Explanation: '.*' means zero or more of any character.
#
# Example 4:
# Input: s = "aab", p = "c*a*b"
# Output: True
# Explanation: "c*" matches zero 'c's, "a*" matches two 'a's,
# and "b" matches "b".


class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        memo = {}

        def match(i, j):

            # Both strings are finished
            if i == len(s) and j == len(p):
                return True

            # Pattern finished but string isn't
            if j == len(p):
                return False

            # Have we already solved this state?
            if (i, j) in memo:
                return memo[(i, j)]

            # Does the current character match?
            first_match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == '.')
            )

            # Check if next pattern character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':

                result = (
                    match(i, j + 2) or
                    (first_match and match(i + 1, j))
                )

            else:

                result = first_match and match(i + 1, j + 1)

            memo[(i, j)] = result

            return result

        return match(0, 0)