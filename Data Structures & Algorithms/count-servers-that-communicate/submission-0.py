class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cols = defaultdict(int)
        rows = defaultdict(int)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (rows[r] > 1 or cols[c] > 1):
                    res += 1
        
        return res