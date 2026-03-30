class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [[grid[0][0], 0, 0]] # [value, r, c]
        visited = set([(0, 0)])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for t in range(n*n):
            while minHeap[0][0] <= t:
                val, r, c = heapq.heappop(minHeap)
                if r == n-1 and c == n-1:
                    return t
                for dR, dC in directions:
                    newR, newC = r+dR, c+dC
                    if min(newR, newC) < 0 or max(newR, newC) >= n or (newR, newC) in visited:
                        continue
                    heapq.heappush(minHeap, [grid[newR][newC], newR, newC])
                    visited.add((newR, newC))