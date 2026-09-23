# Problem 20: Valid Parentheses
# Difficulty: Easy
#
# Description:
# Given a string s containing just the characters '(', ')', '{', '}',
# '[' and ']', determine if the input string is valid.
#
# A string is valid if:
# 1. Open brackets are closed by the same type of bracket.
# 2. Open brackets are closed in the correct order.
# 3. Every closing bracket has a corresponding opening bracket.
#
# Example 1:
# Input: s = "()"
# Output: True
#
# Example 2:
# Input: s = "()[]{}"
# Output: True
#
# Example 3:
# Input: s = "(]"
# Output: False
#
# Example 4:
# Input: s = "([])"
# Output: True
#
# Example 5:
# Input: s = "([)]"
# Output: False


class Solution:

    def isValid(self, s: str) -> bool:

        opened = []

        for i in range(len(s)):

            # Opening brackets
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                opened.append(s[i])

            # Closing parenthesis
            elif s[i] == ')':

                if len(opened) == 0:
                    return False

                elif opened[-1] == '(':
                    opened.pop()

                else:
                    return False

            # Closing square bracket
            elif s[i] == ']':

                if len(opened) == 0:
                    return False

                elif opened[-1] == '[':
                    opened.pop()

                else:
                    return False

            # Closing curly bracket
            elif s[i] == '}':

                if len(opened) == 0:
                    return False

                elif opened[-1] == '{':
                    opened.pop()

                else:
                    return False

        return len(opened) == 0