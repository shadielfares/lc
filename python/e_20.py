class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                stack.append(bracket)
            elif stack and ((bracket == ')' and stack[-1] == '(') or (bracket == '}' and stack[-1] == '{') or (bracket == ']' and stack[-1] == '[')):
                stack.pop()
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False
            