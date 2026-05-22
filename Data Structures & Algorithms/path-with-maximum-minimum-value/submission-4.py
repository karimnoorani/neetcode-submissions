class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_heap = [[-grid[0][0], 0, 0]] # [row, col, path value]
        best = {}

        while max_heap:
            path_value, row, col = heapq.heappop(max_heap)
            path_value *= -1

            if row == ROWS-1 and col == COLS-1:
                return path_value
            
            if (row, col) in best:
                continue
            
            best[(row, col)] = path_value
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                neiR, neiC = row+dr, col+dc
                if min(neiR, neiC) < 0 or neiR == ROWS or neiC == COLS or (neiR, neiC) in best:
                    continue
                heapq.heappush(max_heap, [-min(path_value, grid[neiR][neiC]), neiR, neiC])
        
        return -1