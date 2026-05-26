class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = defaultdict(set)
        distance = defaultdict(int)
        queue = deque()
        total_distance = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        total_houses = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    queue.append([row, col, row, col, 0])
                    total_houses += 1
        
        while queue:
            row, col, originR, originC, dist = queue.popleft()

            if grid[row][col] == 0:
                total_distance[row][col] += dist
            
            for dr, dc in directions:
                neiR, neiC = row+dr, col+dc
                if (min(neiR, neiC) < 0 or neiR == ROWS or 
                    neiC == COLS or grid[neiR][neiC] != 0 or 
                    (originR, originC) in visited[(neiR, neiC)]):
                    continue
                queue.append([neiR, neiC, originR, originC, dist+1])
                visited[(neiR, neiC)].add((originR, originC))
        
        res = float('inf')
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0 and len(visited[(row, col)]) == total_houses:
                    res = min(res, total_distance[row][col])
        
        return res if res < float('inf') else -1