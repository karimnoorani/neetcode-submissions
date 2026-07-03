class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        min_heap = [[grid[0][0], 0, 0]]
        shortest = {(0, 0): 0}

        while min_heap:
            current_time, x, y = heapq.heappop(min_heap)

            if x == ROWS-1 and y == COLS-1:
                return current_time
            
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newX, newY = x+dx, y+dy

                if min(newX, newY) < 0 or newX == ROWS or newY == COLS:
                    continue
                
                newTime = max(current_time, grid[newX][newY])
                
                if (newX, newY) in shortest and newTime >= shortest[(newX, newY)]:
                    continue
                
                heapq.heappush(min_heap, [newTime, newX, newY])
                shortest[(newX, newY)] = newTime