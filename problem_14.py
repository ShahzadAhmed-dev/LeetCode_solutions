# Problem 14: Longest Common Prefix
# Difficulty: Easy
#
# Description:
# Write a function to find the longest common prefix string amongst
# an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: strs = ["flower", "flow", "flight"]
# Output: "fl"
#
# Explanation:
# "fl" is the longest prefix shared by all three strings.
#
# Example 2:
# Input: strs = ["dog", "racecar", "car"]
# Output: ""
#
# Explanation:
# There is no common prefix among the input strings.


class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:

        if len(strs) == 0:
            return ''

        prefix = strs[0]

        for i in range(1, len(strs)):

            while strs[i].find(prefix) != 0:

                prefix = prefix[0 : len(prefix) - 1]

                if prefix == '':
                    return ''

        return prefix