class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS or
                grid[r][c] == 0 or (r, c) in visited):
                return 0
            
            visited.add((r, c))
            res = 1
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                res += dfs(r+dr, c+dc)
            
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, dfs(r, c))
        
        return res