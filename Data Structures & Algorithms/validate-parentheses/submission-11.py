class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closingBrackets = {'}': '{', ']':'[', ')':'('}

        for c in s:
            if c not in closingBrackets:
                stack.append(c)
                continue
            if not stack or closingBrackets[c] != stack.pop():
                return False
        
        return len(stack) == 0