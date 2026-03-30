class Solution:
    def isValid(self, s: str) -> bool:
        closingParams = {'}': '{', ']':'[', ')':'('}
        stack = []

        for c in s:
            if c in closingParams:
                if len(stack) == 0 or stack[-1] != closingParams[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return len(stack) == 0