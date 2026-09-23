# Problem 3524: Find X-Sum of All K-Long Subarrays I
# Difficulty: Medium
#
# Description:
# Given an integer array nums and an integer k, consider every
# non-empty subarray of nums.
#
# For each subarray, calculate the product of all its elements
# modulo k.
#
# Return an array result where result[r] is the number of
# non-empty subarrays whose product modulo k equals r.
#
# Example:
# Input: nums = [1, 2, 3], k = 3
#
# Subarrays:
# [1]       -> 1 % 3 = 1
# [2]       -> 2 % 3 = 2
# [3]       -> 0
# [1, 2]    -> 2 % 3 = 2
# [2, 3]    -> 0
# [1, 2, 3] -> 0
#
# Output:
# [3, 1, 2]
#
# Explanation:
# Product modulo 3 = 0 → 3 subarrays
# Product modulo 3 = 1 → 1 subarray
# Product modulo 3 = 2 → 2 subarrays


class Solution:

    def resultArray(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)

        result = [0] * k

        # dp[r] stores the number of subarrays ending at the
        # previous position whose product modulo k is r.
        dp = [0] * k

        for i in range(n):

            # Stores the subarrays ending at the current position.
            ndp = [0] * k

            # Start a new subarray with nums[i].
            ndp[nums[i] % k] += 1

            # Extend every previous subarray with nums[i].
            for r in range(k):

                ndp[(r * nums[i]) % k] += dp[r]

            # Move to the current state.
            dp = ndp

            # Add the current subarrays to the final answer.
            for r in range(k):

                result[r] += dp[r]

        return result