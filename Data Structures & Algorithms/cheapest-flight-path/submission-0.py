from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = {i:[] for i in range(n)}
        
        for flightSRC, flightDST, price in flights:
            adjList[flightSRC].append([flightDST, price])
        
        stops = -1

        flightQueue = deque([[src, 0]])

        minPrice = float('inf')

        while flightQueue and stops <= k:
            qLen = len(flightQueue)
            for i in range(qLen):
                flightDST, price = flightQueue.popleft()
                if flightDST == dst:
                    minPrice = min(minPrice, price)
                else:
                    for neighbor, neighborPrice in adjList[flightDST]:
                        flightQueue.append([neighbor, price+neighborPrice])
            stops += 1
        
        return minPrice if minPrice < float('inf') else -1