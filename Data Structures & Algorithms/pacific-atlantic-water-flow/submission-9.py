class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl = set()
        pac = set()

        def dfs(r, c, visit, prev):
            if (min(r, c) < 0 or r >= ROWS or c >= COLS 
                or (r, c) in visit or heights[r][c] < prev):
                return
            
            visit.add((r, c))
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                dfs(r+dr, c+dc, visit, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, float('-INF'))
            dfs(ROWS-1, c, atl, float('-INF'))
        
        for r in range(ROWS):
            dfs(r, 0, pac, float('-INF'))
            dfs(r, COLS-1, atl, float('-INF'))
        
        return list(atl & pac)

