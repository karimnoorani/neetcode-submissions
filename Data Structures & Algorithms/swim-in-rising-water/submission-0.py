import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        shortest = {}
        minHeap = [[grid[0][0], (0, 0)]]
        
        while (ROWS-1, COLS-1) not in shortest:
            weight, point = heapq.heappop(minHeap)
            r, c = point

            if point in shortest:
                continue
            
            shortest[point] = weight

            neighbors = [(r+1, c), (r, c+1), (r-1, c), (r,c-1)]
            for neighbor in neighbors:
                r, c = neighbor
                if (min(r, c) < 0 or r == ROWS or c == COLS
                    or (r,c) in shortest):
                    continue
                
                heapq.heappush(minHeap, [max(weight, grid[r][c]), (r, c)])
        
        return shortest[(ROWS-1, COLS-1)]