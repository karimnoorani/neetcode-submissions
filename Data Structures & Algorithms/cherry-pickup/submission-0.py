class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        memo = {}

        def dfs(r1, c1, r2, c2):
            if min(r1, r2, c1, c2) < 0 or max(r1, r2, c1, c2) >= n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            
            if (r1, c1, r2, c2) in memo:
                return memo[(r1, c1, r2, c2)]

            if r1 == n-1 and c1 == n-1:
                return grid[r1][c1]
            
            cherries = grid[r1][c1]
            if r1 != r2 or c1 != c2:
                cherries += grid[r2][c2]
            
            res = max(
                dfs(r1+1, c1, r2+1, c2),
                dfs(r1+1, c1, r2, c2+1),
                dfs(r1, c1+1, r2+1, c2),
                dfs(r1, c1+1, r2, c2+1)
            )
            
            memo[(r1, c1, r2, c2)] = cherries + res
            return memo[(r1, c1, r2, c2)]
        
        res = dfs(0, 0, 0, 0)
        return max(0, res)