class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def DFS(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS
                or (r, c) in visited or grid[r][c] == "0"):
                return
            
            visited.add((r, c))
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                DFS(r+dR, c+dC)
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    DFS(r, c)
        
        return islands