from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        def getNeighbors(r, c):
            return ([(r+1, c), (r, c+1), (r-1, c), (r, c-1)])
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        visited = set()
        queue = deque()
        queue.append((0,0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return length
                
                neighbors = getNeighbors(r,c)
                for neighbor in neighbors:
                    nR, nC = neighbor
                    if (min(nR, nC) < 0 or nR == ROWS 
                        or nC == COLS or (nR, nC) in visited
                        or grid[nR][nC] == 1):
                        continue
                    
                    queue.append((nR, nC))
                    visited.add((nR, nC))
            length += 1
        
        return -1
