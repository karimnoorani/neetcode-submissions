class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = defaultdict(set)
        total = defaultdict(int)
        count = defaultdict(int)
        totalBuildings = 0
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append([r, c, r, c, 0])
                    totalBuildings += 1
        
        while q:
            r, c, originR, originC, steps = q.popleft()
            
            if grid[r][c] == 0:
                total[(r, c)] += steps
                count[(r, c)] += 1
            
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newR, newC = r+dR, c+dC
                if (min(newR, newC) < 0 or newR == ROWS or newC == COLS 
                    or (newR, newC) in visited[(originR, originC)]
                    or grid[newR][newC] != 0):
                    continue
                q.append([newR, newC, originR, originC, steps+1])
                visited[(originR, originC)].add((newR, newC))
        
        ans = float('inf')
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0 and count[(r, c)] == totalBuildings:
                    ans = min(ans, total[(r, c)])

        return ans if ans != float('inf') else -1