# Problem 1: Two Sum
# Difficulty: Easy
#
# Description:
# Given an array of integers and a target value, find two numbers
# whose sum equals the target and return their indices.
#
# Example 1:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9.
#
# Example 2:
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Explanation: nums[1] + nums[2] = 2 + 4 = 6.


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):

            for j in range(len(nums)):

                if i != j and (nums[j] + nums[i] == target):

                    return [i, j]