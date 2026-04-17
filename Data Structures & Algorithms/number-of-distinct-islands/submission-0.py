class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = set()
        visited = set()

        def dfs(r, c):
            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] != 1:
                return
            
            visited.add((r, c))
            current_island.append((r_origin-r, c_origin-c))
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(r+dR, c+dC)
        
        for r in range(ROWS):
            for c in range(COLS):
                current_island = []
                r_origin = r
                c_origin = c
                dfs(r, c)

                if current_island:
                    islands.add(tuple(current_island))
        
        return len(islands)