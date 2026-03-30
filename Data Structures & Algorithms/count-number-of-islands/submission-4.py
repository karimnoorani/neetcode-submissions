from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited = set()

        def dfs(r, c):
            
            if (r, c) in visited:
                return
            
            visited.add((r, c))

            neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]

            for r, c in neighbors:
                if (min(r, c) < 0 or r >= ROWS or c >= COLS
                    or (r, c) in visited or grid[r][c] == "0"):
                    continue
                
                dfs(r, c)
        
        islandCount = 0 
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    dfs(r, c)
                    islandCount += 1
        
        return islandCount
        