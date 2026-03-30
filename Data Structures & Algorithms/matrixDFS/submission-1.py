class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        def dfs(grid, r, c, visited):
            if (min(r, c) < 0 or r == len(grid)
                or c == len(grid[0]) or grid[r][c]== 1
                or (r,c) in visited):
                return 0
            if r == len(grid)-1 and c == len(grid[0])-1:
                return 1
            
            visited.add((r, c))

            count = 0
            count += dfs(grid, r + 1, c, visited)
            count += dfs(grid, r, c + 1, visited)
            count += dfs(grid, r - 1, c, visited)
            count += dfs(grid, r, c - 1, visited)

            visited.remove((r, c))
            return count
        
        return dfs(grid, 0, 0, set())