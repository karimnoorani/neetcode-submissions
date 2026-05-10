class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, ocean):
            ocean.add((r, c))

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                neiR, neiC = r+dr, c+dc
                if (min(neiR, neiC) < 0 or neiR == ROWS or 
                    neiC == COLS or (neiR, neiC) in ocean or
                    heights[neiR][neiC] < heights[r][c]):
                    continue
                
                dfs(neiR, neiC, ocean)
        
        for col in range(COLS):
            dfs(0, col, pac)
            dfs(ROWS-1, col, atl)
        
        for row in range(ROWS):
            dfs(row, 0, pac)
            dfs(row, COLS-1, atl)
        
        return list(pac & atl)