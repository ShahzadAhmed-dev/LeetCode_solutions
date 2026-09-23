# Problem 1658: Minimum Operations to Reduce X to Zero
# Difficulty: Medium
#
# Description:
# You are given an integer array nums and an integer x.
#
# In one operation, you can remove the leftmost or rightmost
# element from nums and subtract its value from x.
#
# Return the minimum number of operations to reduce x exactly to 0.
# If it is impossible, return -1.
#
# Example 1:
# Input: nums = [1, 1, 4, 2, 3], x = 5
# Output: 2
# Explanation:
# Remove 3 from the right and 2 from the right.
#
# Example 2:
# Input: nums = [5, 6, 7, 8, 9], x = 4
# Output: -1
#
# Example 3:
# Input: nums = [3, 2, 20, 1, 1, 3], x = 10
# Output: 5


class Solution:

    def minOperations(self, nums: list[int], x: int) -> int:

        total = sum(nums)

        target = total - x

        if target < 0:
            return -1

        left = 0
        current = 0
        longest = -1

        for right in range(len(nums)):

            current += nums[right]

            while current > target and left <= right:
                current -= nums[left]
                left += 1

            if current == target:
                longest = max(
                    longest,
                    right - left + 1
                )

        if longest == -1:
            return -1

        return len(nums) - longest