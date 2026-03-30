class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def DFS(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS 
                or (r, c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            area = 1
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                area += DFS(r+dR, c+dC)
            
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, DFS(r, c))
        
        return res