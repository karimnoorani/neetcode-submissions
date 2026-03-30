class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def dfs(i, j):
            if min(i, j) < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0" or (i, j) in visited:
                return
            
            visited.add((i, j))

            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)

            return
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    print(i, j)
                    islands += 1
        
        return islands
