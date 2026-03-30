class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pac, atl = {}, {}

        def getNeighbors(r, c, visited):
            neighbors = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
            for neighbor in neighbors.copy():
                nR, nC = neighbor
                if (min(nR, nC) < 0 or nR == ROWS or nC == COLS
                    or (nR, nC) in visited or heights[r][c] < heights[nR][nC]):
                    neighbors.remove(neighbor)
            return neighbors
        
        def canReachPacific(r, c, visited):
            # if (r, c) in pac:
            #     return pac[(r, c)]

            if r == 0 or c == 0:
                pac[(r, c)] = True
                return True
            visited.add((r, c))
            neighbors = getNeighbors(r, c, visited)
            if len(neighbors) == 0:
                pac[(r, c)] = False
                return False
            canNeighborsReach = []
            for neighbor in neighbors:
                canNeighborsReach.append(canReachPacific(neighbor[0], neighbor[1], visited))
            pac[(r, c)] = True if True in canNeighborsReach else False
            return True if True in canNeighborsReach else False
        
        def canReachAtlantic(r, c, visited):
            # if (r, c) in atl:
            #     return atl[(r, c)]
            
            if r == ROWS-1 or c == COLS-1:
                atl[(r, c)] = True
                return True

            visited.add((r, c))
            neighbors = getNeighbors(r, c, visited)
            if len(neighbors) == 0:
                atl[(r, c)] = False
                return False
            canNeighborsReach = []
            for neighbor in neighbors:
                canNeighborsReach.append(canReachAtlantic(neighbor[0], neighbor[1], visited))
            atl[(r, c)] = True if True in canNeighborsReach else False
            return True if True in canNeighborsReach else False
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if canReachPacific(r, c, set()) and canReachAtlantic(r, c, set()):
                    res.append([r, c])
        
        print(pac)
        print(atl)

        return res