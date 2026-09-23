# Problem 3: Longest Substring Without Repeating Characters
# Difficulty: Medium
#
# Description:
# Given a string s, find the length of the longest substring
# without repeating characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with a length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with a length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with a length of 3.


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:

        subStr = set()
        maximum = 0
        left = 0

        for i in range(len(s)):

            while s[i] in subStr:
                subStr.remove(s[left])
                left += 1

            subStr.add(s[i])

            maximum = max(maximum, i - left + 1)

        return maximum