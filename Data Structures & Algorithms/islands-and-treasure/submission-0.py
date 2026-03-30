from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        q = deque()
        visited = set()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r, c))
        
        distance = 1
        while q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
                for neighbor in neighbors:
                    r, c = neighbor
                    if (min(r, c) < 0 or r == ROWS or c == COLS
                        or (r, c) in visited or grid[r][c] != 2147483647):
                        continue
                    grid[r][c] = distance
                    visited.add((r, c))
                    q.append((r, c))
            distance += 1

