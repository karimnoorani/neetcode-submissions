class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minHeap = [[grid[0][0], 0, 0]] # [value, r, c]
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == n-1 and c == n-1:
                return t
            if (r, c) in visited:
                continue
            visited.add((r, c))
            for dR, dC in directions:
                newR, newC = r+dR, c+dC
                if min(newR, newC) < 0 or max(newR, newC) >= n or (newR, newC) in visited:
                    continue
                heapq.heappush(minHeap, [max(t, grid[newR][newC]), newR, newC])