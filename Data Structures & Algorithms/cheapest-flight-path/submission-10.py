class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i: [] for i in range(n)}

        for from_i, to_i, price_i in flights:
            adjList[from_i].append([price_i, to_i])
        
        minHeap = [[0, 0, src]] # [price, stops, node]
        best_stops = [float('inf') for _ in range(n)]

        while minHeap:
            price, stops, node = heapq.heappop(minHeap)

            if node == dst:
                return price
            
            if stops > k or stops >= best_stops[node]:
                continue
            
            best_stops[node] = stops
            for neiPrice, nei in adjList[node]:
                heapq.heappush(minHeap, [price+neiPrice, stops+1, nei])
        
        return -1