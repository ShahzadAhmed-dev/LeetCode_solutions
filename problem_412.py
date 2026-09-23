# Problem 412: Fizz Buzz
# Difficulty: Easy
#
# Description:
# Given an integer n, return a string array answer (1-indexed) where:
#
# - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# - answer[i] == "Fizz" if i is divisible by 3.
# - answer[i] == "Buzz" if i is divisible by 5.
# - answer[i] == i as a string in any other case.
#
# Example 1:
# Input: n = 3
# Output: ["1", "2", "Fizz"]
#
# Example 2:
# Input: n = 5
# Output: ["1", "2", "Fizz", "4", "Buzz"]
#
# Example 3:
# Input: n = 15
# Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7",
#          "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]


class Solution:

    def fizzBuzz(self, n: int) -> list[str]:

        ans = []
        count = 0

        while n > 0:

            count += 1
            ans.append(count)
            n -= 1

        for i in range(len(ans)):

            if ans[i] % 3 == 0 and ans[i] % 5 == 0:
                ans[i] = "FizzBuzz"

            elif ans[i] % 3 == 0:
                ans[i] = "Fizz"

            elif ans[i] % 5 == 0:
                ans[i] = "Buzz"

        for i in range(len(ans)):

            ans[i] = str(ans[i])

        return ans