# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        for char in s:
            if char not in closeToOpen:
                stack.append(char)
            elif not stack or stack[-1] != closeToOpen[char]:
                return False
            else:
                stack.pop()

        return len(stack) == 0