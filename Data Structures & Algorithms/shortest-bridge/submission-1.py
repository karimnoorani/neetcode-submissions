class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        def dfs(row, col):
            if min(row, col) < 0 or row == ROWS or col == COLS or (row, col) in visited:
                return
            
            visited.add((row, col))
            if grid[row][col] == 0:
                queue.append([row, col, 0])
                return
            
            for dr, dc in directions:
                dfs(row+dr, col+dc)
        
        def fillNeighbors():
            for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col] == 1:
                        dfs(row, col)
                        return
        
        fillNeighbors()

        while queue:
            row, col, dist = queue.popleft()

            if grid[row][col] == 1:
                return dist
            
            for dr, dc in directions:
                neiR, neiC = row+dr, col+dc
                if min(neiR, neiC) < 0 or neiR == ROWS or neiC == COLS or (neiR, neiC) in visited:
                    continue
                visited.add((neiR, neiC))
                queue.append([neiR, neiC, dist+1])