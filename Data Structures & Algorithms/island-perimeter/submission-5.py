class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def getPerimeter(r, c):
            perimeter = 4
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if (0 <= (r + dR) < ROWS and 0 <= (c + dC) < COLS
                    and grid[(r+dR)][c+dC] == 1):
                    perimeter -= 1
            return perimeter

        def dfs(r, c):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS
                or (r, c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r, c))
            perimeter = getPerimeter(r, c)
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                perimeter += dfs(r+dR, c+dC)
            
            return perimeter
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)