class Solution:
    def isValid(self, s: str) -> bool:
        closingBrackets = {']': '[', ')': '(', '}': '{'}
        stack = []

        for c in s:
            if c not in closingBrackets:
                stack.append(c)
                continue
            
            if not stack or closingBrackets[c] != stack[-1]:
                return False
            
            stack.pop()
        
        return len(stack) == 0