# Problem 3525: Find X-Sum of All K-Long Subarrays II
# Difficulty: Hard
#
# Description:
# You are given an integer array nums, an integer k, and a list
# of queries.
#
# Each query contains:
# [index, value, start, x]
#
# For each query:
# 1. Update nums[index] = value.
# 2. Consider the subarray nums[start:].
# 3. Count the number of non-empty subarrays whose product modulo k
#    is equal to x.
# 4. Add that count to the answer.
#
# A segment tree is used to efficiently handle both updates and
# range queries.
#
# Example:
# nums = [1, 2, 3]
# k = 3
# queries = [[1, 4, 0, 1]]
#
# After the update:
# nums = [1, 4, 3]
#
# The segment tree is then queried for the range [0, 2].


class SegmentTree:

    def __init__(self, nums: List[int], k: int):

        self.k = k

        n = len(nums)
        size = 2 << n.bit_length()

        # tree[o] stores:
        # [number of subarrays by remainder] + [product of interval]
        self.tree = [[0] * (k + 1) for _ in range(size)]

        self.build(nums, 1, 0, n - 1)

    def makeLeaf(self, o: int, value: int) -> None:

        info = [0] * (self.k + 1)

        r = value % self.k

        # The single element forms one subarray.
        info[r] = 1

        # Store the product of the interval.
        info[self.k] = r

        self.tree[o] = info

    def mergePre(
        self,
        left: List[int],
        right: List[int]
    ) -> List[int]:

        pre = [0] * (self.k + 1)

        mul_L = left[self.k]
        mul_R = right[self.k]

        # Product of the entire interval.
        pre[self.k] = (mul_L * mul_R) % self.k

        # Subarrays completely inside the left interval.
        for x in range(self.k):
            pre[x] = left[x]

        # Subarrays that contain the entire left interval
        # followed by a prefix of the right interval.
        for x in range(self.k):
            pre[(mul_L * x) % self.k] += right[x]

        return pre

    def maintain(self, o: int) -> None:

        self.tree[o] = self.mergePre(
            self.tree[o * 2],
            self.tree[o * 2 + 1]
        )

    def build(
        self,
        nums: List[int],
        o: int,
        l: int,
        r: int
    ) -> None:

        if l == r:
            self.makeLeaf(o, nums[l])
            return

        m = (l + r) // 2

        self.build(nums, o * 2, l, m)
        self.build(nums, o * 2 + 1, m + 1, r)

        self.maintain(o)

    def update(
        self,
        o: int,
        l: int,
        r: int,
        index: int,
        value: int
    ) -> None:

        if l == r:
            self.makeLeaf(o, value)
            return

        m = (l + r) // 2

        if index <= m:
            self.update(o * 2, l, m, index, value)

        else:
            self.update(o * 2 + 1, m + 1, r, index, value)

        self.maintain(o)

    def query(
        self,
        o: int,
        l: int,
        r: int,
        L: int,
        R: int
    ) -> List[int]:

        # The current segment is completely inside
        # the requested range.
        if L <= l and r <= R:
            return self.tree[o]

        m = (l + r) // 2

        if R <= m:
            return self.query(o * 2, l, m, L, R)

        if L > m:
            return self.query(o * 2 + 1, m + 1, r, L, R)

        left = self.query(o * 2, l, m, L, R)
        right = self.query(o * 2 + 1, m + 1, r, L, R)

        return self.mergePre(left, right)


class Solution:

    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)

        seg = SegmentTree(nums, k)

        ans = []

        for index, value, start, x in queries:

            # Update nums[index].
            seg.update(
                1,
                0,
                n - 1,
                index,
                value
            )

            # Query the range [start, n - 1].
            pre = seg.query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            # pre[x] contains the number of subarrays
            # whose product modulo k equals x.
            ans.append(pre[x])

        return ans