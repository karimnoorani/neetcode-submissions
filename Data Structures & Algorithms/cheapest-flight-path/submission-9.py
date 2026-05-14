class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i: [] for i in range(n)}

        for from_i, to_i, price_i in flights:
            adjList[from_i].append([price_i, to_i])
        
        minHeap = [[0, 0, src]] # [price, stops, node]
        res = float('inf')

        while minHeap:
            price, stops, node = heapq.heappop(minHeap)

            if node == dst:
                return price
            
            if stops > k:
                continue
            
            for neiPrice, nei in adjList[node]:
                heapq.heappush(minHeap, [price+neiPrice, stops+1, nei])
        
        return res if res != float('inf') else -1