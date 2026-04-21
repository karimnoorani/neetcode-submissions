class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dist_grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        visited = defaultdict(set)
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append([r, c, r, c, 0]) # [r, c, origin_r, origin_c, steps]
                    visited[(r, c)].add((r, c))
        
        while q:
            r, c, origin_r, origin_c, steps = q.popleft()
            
            dist_grid[r][c] += steps

            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                neiR, neiC = r+dR, c+dC
                if min(neiR, neiC) < 0 or neiR == ROWS or neiC == COLS or (neiR, neiC) in visited[(origin_r, origin_c)]:
                    continue
                q.append([neiR, neiC, origin_r, origin_c, steps+1])
                visited[(origin_r, origin_c)].add((neiR, neiC))
        
        res = float('inf')
        for r in range(ROWS):
            for c in range(COLS):
                res = min(res, dist_grid[r][c])
        print(dist_grid[r][c])
        return res