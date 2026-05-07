class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = [[0, points[0][0], points[0][1]]]
        total = 0
        visited = set()

        while len(visited) < len(points):
            cost, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue
            
            total += cost
            visited.add((r, c))

            for neiR, neiC in points:
                if (neiR, neiC) in visited:
                    continue
                
                heapq.heappush(minHeap, [abs(r-neiR)+abs(c-neiC), neiR, neiC])
        
        return total
