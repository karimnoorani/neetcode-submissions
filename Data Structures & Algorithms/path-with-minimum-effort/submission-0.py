import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [[0, (0, 0)]] # [maxEffort, point]
        visited = set()
        ROWS, COLS = len(heights), len(heights[0])

        while heap:
            maxEffort, point = heapq.heappop(heap)

            if point == (ROWS-1, COLS-1):
                return maxEffort
            
            if point in visited:
                continue

            r, c = point
            visited.add((r, c))
            for dR, dC in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                neiR, neiC = r+dR, c+dC
                if min(neiR, neiC) < 0 or neiR >= ROWS or neiC >= COLS or (neiR, neiC) in visited:
                    continue
                heapq.heappush(heap, [max(maxEffort, abs(heights[neiR][neiC]-heights[r][c])), (neiR, neiC)])
                