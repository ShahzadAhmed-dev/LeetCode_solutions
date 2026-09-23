# Problem 27: Remove Element
# Difficulty: Easy
#
# Description:
# Given an integer array nums and an integer val, remove all
# occurrences of val in nums in-place.
#
# The order of the remaining elements may be changed.
#
# Return k, the number of elements in nums that are not equal to val.
#
# Example 1:
# Input: nums = [3, 2, 2, 3], val = 3
# Output: 2
# Explanation: The first two elements of nums should be [2, 2].
#
# Example 2:
# Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# Output: 5
# Explanation: The first five elements of nums should contain
# [0, 1, 3, 0, 4].


class Solution:

    def removeElement(self, nums: list[int], val: int) -> int:

        k = 0

        for i in range(len(nums)):

            if nums[i] != val:

                nums[k] = nums[i]
                k += 1

        return k