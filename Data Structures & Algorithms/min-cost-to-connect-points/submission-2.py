import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [[0, points[0]]]
        visited = set()
        res = 0

        while heap:
            w, point = heapq.heappop(heap)
            xi, yi = point
            
            if (xi, yi) in visited:
                continue
            
            visited.add((xi, yi))
            res += w

            for xj, yj in points:
                if (xj, yj) in visited:
                    continue
                
                heapq.heappush(heap, [abs(xi-xj)+abs(yi-yj), (xj, yj)])
        
        return res