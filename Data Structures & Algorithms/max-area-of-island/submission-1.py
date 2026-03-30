class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def getNeighbors(r, c):
            return ([(r+1,c), (r,c+1), (r-1,c), (r,c-1)])
        
        def dfs(grid, r, c):
            if (min(r, c) < 0 or (r,c) in visited 
                or r == len(grid) or c == len(grid[0])
                or grid[r][c] == 0):
                return 0
            
            visited.add((r,c))

            neighbors = getNeighbors(r,c)
            area = 1
            for neighbor in neighbors:
                area += dfs(grid, neighbor[0], neighbor[1])
            
            return area
        
        maxArea = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r,c) not in visited:
                    maxArea = max(maxArea, dfs(grid, r, c))
        
        return maxArea