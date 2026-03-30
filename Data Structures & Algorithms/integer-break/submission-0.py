class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {0: 1, 1: 1, 2: 1}
        def dfs(n):
            if n in cache:
                return cache[n]
            
            res = 1
            for i in range(2, n):
                res = max(res, i*dfs(n-i), i*(n-i))
            cache[n] = res
            return cache[n]

        return dfs(n)