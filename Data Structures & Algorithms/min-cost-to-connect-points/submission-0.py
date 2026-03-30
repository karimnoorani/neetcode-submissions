import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost = 0
        visited = set()
        minHeap = [[0, (points[0][0], points[0][1])]]
        while minHeap:
            w, p = heapq.heappop(minHeap)
            print(p)
            if p in visited:
                continue
            
            visited.add(p)
            x, y = p
            cost += w
            for x1, y1 in points:
                if (x1, y1) in visited:
                    continue
                heapq.heappush(minHeap, (abs(x-x1)+abs(y-y1), (x1, y1)))
        
        return cost
