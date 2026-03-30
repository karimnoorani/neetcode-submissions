from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        q.append((r+dR, c+dC))
        
        distance = 1
        while q:
            qLen = len(q)
            for _ in range(qLen):
                r, c = q.popleft()

                if min(r, c) < 0 or r >= ROWS or c >= COLS or grid[r][c] != 2147483647:
                    continue
                
                grid[r][c] = distance
                for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    q.append((r+dR, c+dC))
            distance += 1
        