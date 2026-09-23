# Problem 4: Median of Two Sorted Arrays
# Difficulty: Hard
#
# Description:
# Given two sorted arrays nums1 and nums2, return the median
# of the two sorted arrays.
#
# Example 1:
# Input: nums1 = [1, 3], nums2 = [2]
# Output: 2.0
# Explanation: The merged array is [1, 2, 3].
# The median is 2.
#
# Example 2:
# Input: nums1 = [1, 2], nums2 = [3, 4]
# Output: 2.5
# Explanation: The merged array is [1, 2, 3, 4].
# The median is (2 + 3) / 2 = 2.5.


class Solution:

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        new_array = []

        new_array.extend(nums1)
        new_array.extend(nums2)
        new_array.sort()

        if len(new_array) % 2 == 0:

            mid1 = len(new_array) // 2 - 1
            mid2 = len(new_array) // 2

            median = (new_array[mid1] + new_array[mid2]) / 2

            return median

        else:

            median2 = len(new_array) // 2

            return new_array[median2]