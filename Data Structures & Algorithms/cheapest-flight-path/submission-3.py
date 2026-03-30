class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        for from_i, to_i, price in flights:
            adj[from_i].append([price, to_i])
        
        minHeap = [[0, src, k+1]]

        while minHeap:
            cost, node, k = heapq.heappop(minHeap)

            if node == dst:
                return cost

            if k == 0:
                continue
            

            for neiCost, nei in adj[node]:
                heapq.heappush(minHeap, [cost+neiCost, nei, k-1])
        
        return -1