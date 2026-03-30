from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        q = deque()
        visited = set()

        q.append((0,0))
        length = 0
        while q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                if (min(r, c) < 0 or r == ROWS or c == COLS
                    or (r, c) in visited or grid[r][c] == 1):
                    continue
                
                if r == ROWS-1 and c == COLS-1:
                    return length

                visited.add((r, c))

                q.append((r+1, c))
                q.append((r, c+1))
                q.append((r-1, c))
                q.append((r, c-1))
            length += 1
        
        return -1