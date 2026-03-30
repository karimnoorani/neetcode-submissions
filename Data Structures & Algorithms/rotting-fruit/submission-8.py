class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))

        minutes = 0 if not q else -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2

                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nR, nC = r+dr, c+dc
                    if min(nR, nC) < 0 or nR >= ROWS or nC >= COLS or grid[nR][nC] != 1:
                        continue
                    q.append((nR, nC))
            
            minutes += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        
        return minutes