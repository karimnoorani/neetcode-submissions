class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            
            res = 1
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newR, newC = r+dR, c+dC
                if min(newR, newC) < 0 or newR == ROWS or newC == COLS or matrix[newR][newC] <= matrix[r][c]:
                    continue
                res = max(res, 1+dfs(r+dR, c+dC))
            
            cache[(r, c)] = res
            return cache[(r, c)]
        
        res = 1
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))
        
        return res