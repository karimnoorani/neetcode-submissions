class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cache = {}
        def dfs(r, c):
            if r == ROWS-1 and c == COLS-1:
                return grid[r][c]
            
            if (r, c) in cache:
                return cache[(r, c)]
            
            if r >= ROWS or c >= COLS:
                return float('INF')

            cache[(r, c)] = min(grid[r][c]+dfs(r+1, c), grid[r][c]+dfs(r, c+1))
            return cache[(r, c)]
        
        return dfs(0, 0)
