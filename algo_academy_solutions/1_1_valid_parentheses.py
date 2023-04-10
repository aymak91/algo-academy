# https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s):

        stack = []
        closeToOpen = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        for char in s:
            if char not in closeToOpen:
                stack.append(char)
                continue
            
            if not stack or stack[-1] != closeToOpen[char]:
                return False
            stack.pop()    

        return len(stack) == 0