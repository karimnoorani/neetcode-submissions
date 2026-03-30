from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        minutes = 0
        while q:
            qLen = len(q)
            for _ in range(qLen):
                r, c = q.popleft()
                
                for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    newR, newC = r+dR, c+dC
                    if (min(newR, newC) < 0 or newR >= ROWS or newC >= COLS
                        or grid[newR][newC] != 1):
                        continue
                    grid[newR][newC] = 2
                    q.append((newR, newC))
            if q:
                minutes += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return minutes