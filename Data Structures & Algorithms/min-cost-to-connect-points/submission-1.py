class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost = 0
        minHeap = [[0, points[0][0], points[0][1]]] # [cost, x, y]
        visited = set()

        while minHeap:
            pCost, x, y = heapq.heappop(minHeap)

            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            cost += pCost

            if len(visited) == len(points):
                return cost
            
            for nX, nY in points:
                if (nX, nY) in visited:
                    continue
                neiCost = abs(x-nX)+abs(y-nY)
                heapq.heappush(minHeap, [neiCost, nX, nY])