from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    q.append((r,c))
        
        minute = 0

        while q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                neighbors = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]
                for neighbor in neighbors:
                    r, c = neighbor
                    if (min(r,c) < 0 or r == ROWS or c == COLS or 
                    (r, c) in visited or grid[r][c] == 0):
                        continue
                    visited.add((r,c))
                    q.append((r, c))
            
            if len(q) > 0:
                minute += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    return -1
        
        return minute