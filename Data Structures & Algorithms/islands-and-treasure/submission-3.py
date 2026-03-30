from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            r, c = q.popleft()
            
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newR, newC = r+dR, c+dC
                if min(newR, newC) < 0 or newR >= ROWS or newC >= COLS or grid[newR][newC] != 2147483647:
                    continue
                grid[newR][newC] = grid[r][c] + 1
                q.append((newR, newC))
        