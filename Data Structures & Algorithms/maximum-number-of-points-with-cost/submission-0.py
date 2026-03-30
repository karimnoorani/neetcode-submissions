class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ROWS, COLS = len(points), len(points[0])
        cache = {}

        def dfs(r, c):
            if r == ROWS-1:
                return points[r][c]
            
            if (r, c) in cache:
                return cache[(r, c)]

            cache[(r, c)] = points[r][c]
            for i in range(COLS):
                cache[(r, c)] = max(cache[(r, c)], points[r][c]+dfs(r+1, i)-abs(i-c))
            
            return cache[(r, c)]
        
        res = 0
        for c in range(COLS):
            res = max(res, dfs(0, c))
        
        return res