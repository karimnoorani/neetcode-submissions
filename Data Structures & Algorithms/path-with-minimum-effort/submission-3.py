class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        heap = [[0, (0, 0)]]
        visited = set()

        while heap:
            w, p = heapq.heappop(heap)
            r, c = p
            
            if (r, c) in visited:
                continue
            
            if r == ROWS-1 and c == COLS-1:
                return w
            
            visited.add((r, c))
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newR, newC = r+dr, c+dc
                if min(newR, newC) < 0 or newR >= ROWS or newC >= COLS or (newR, newC) in visited:
                    continue
                heapq.heappush(heap, [max(w, abs(heights[r][c]-heights[newR][newC])), (newR, newC)])