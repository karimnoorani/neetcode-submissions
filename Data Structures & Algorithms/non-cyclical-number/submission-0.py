class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def helper(n):
            if n == 1:
                return True
            
            if n in seen:
                return False

            seen.add(n)
            res = 0
            for c in str(n):
                res += int(c) ** 2
            
            return helper(res)
        
        return helper(n)