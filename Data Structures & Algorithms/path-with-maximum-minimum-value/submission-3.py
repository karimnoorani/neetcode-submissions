class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxHeap = [[-grid[0][0], 0, 0]]
        visited = set()

        while maxHeap:
            score, r, c = heapq.heappop(maxHeap)
            score *= -1

            if (r, c) in visited:
                continue
            
            if r == ROWS-1 and c == COLS-1:
                return score
            
            visited.add((r, c))
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                neiR, neiC = r+dR, c+dC
                if min(neiR, neiC) < 0 or neiR == ROWS or neiC == COLS or (neiR, neiC) in visited:
                    continue
                heapq.heappush(maxHeap, [-min(score, grid[neiR][neiC]), neiR, neiC])