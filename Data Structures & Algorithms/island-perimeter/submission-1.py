class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        def getCellPerimeter(r, c):
            neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
            validNeighbors = 0
            for r1, c1 in neighbors:
                if (min(r1, c1) < 0 or r1 >= ROWS or c1 >= COLS
                    or grid[r1][c1] == 0):
                    continue
                validNeighbors += 1
            return 4 - validNeighbors
        
        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS 
                or (r, c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]

            res = getCellPerimeter(r, c)
            for r1, c1 in neighbors:
                res += dfs(r1, c1)
            
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        
        return res