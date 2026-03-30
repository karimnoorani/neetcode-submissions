from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def getNeighbors(r, c):
            neighbors = [[r-1, c], [r, c-1], [r+1, c], [r, c+1]]
            return neighbors
    
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        islandCount = 0

        def BFS(grid, r, c):
            q = deque()
            q.append((r, c))

            while q:
                qLen = len(q)
                for i in range(qLen):
                    nR, nC = q.popleft()
                    # if (min(nR, nC) < 0 or nR == ROWS
                    #     or nC == COLS or (nR, nC) in visited):
                    #     continue
                    visited.add((nR, nC))
                    neighbors = getNeighbors(nR, nC)
                    for neighbor in neighbors:
                        r2, c2 = neighbor
                        if (min(r2, c2) < 0 or r2 == ROWS
                        or c2 == COLS or (r2, c2) in visited
                        or grid[r2][c2] == "0"):
                            continue
                        else:
                            q.append((r2, c2))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    BFS(grid, r, c)
                    islandCount += 1
        
        return islandCount
        