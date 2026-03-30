class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        openCount = 0

        for c in s:
            if c == '(':
                openCount += 1
                res = max(res, openCount)
            elif c == ')':
                openCount -= 1
        
        return res