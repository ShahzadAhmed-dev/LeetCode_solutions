# Problem 5: Longest Palindromic Substring
# Difficulty: Medium
#
# Description:
# Given a string s, return the longest palindromic substring in s.
#
# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"
# Explanation: "bb" is the longest palindromic substring.


class Solution:

    def longestPalindrome(self, s: str) -> str:

        longest = ''

        for start in range(len(s)):

            for end in range(start, len(s)):

                sub = s[start:end+1]

                if sub == sub[::-1]:

                    if len(sub) > len(longest):
                        longest = sub

        return longest