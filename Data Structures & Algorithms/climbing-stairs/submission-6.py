class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {0: 0, 1: 1, 2: 2}

        def dfs(n):
            if n in cache:
                return cache[n]
            
            cache[n] = dfs(n-1) + dfs(n-2)

            return cache[n]
        
        return dfs(n)