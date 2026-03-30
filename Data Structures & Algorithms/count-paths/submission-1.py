class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {(m-1, n-1): 1}
        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            
            if min(r, c) < 0 or r >= m or c >= n:
                return 0
            
            paths = 0
            for dR, dC in [(1, 0), (0, 1)]:
                paths += dfs(r+dR, c+dC)
            
            cache[(r, c)] = paths
            return cache[(r, c)]
        
        return dfs(0, 0)