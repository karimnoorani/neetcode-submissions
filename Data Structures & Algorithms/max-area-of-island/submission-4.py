class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if (min(row, col) < 0 or row == ROWS or col == COLS
                or (row, col) in visited or grid[row][col] == 0):
                return 0
            
            visited.add((row, col))
            area = 1
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                area += dfs(row+dr, col+dc)
            
            return area
        
        maxArea = 0
        for row in range(ROWS):
            for col in range(COLS):
                maxArea = max(maxArea, dfs(row, col))
        
        return maxArea