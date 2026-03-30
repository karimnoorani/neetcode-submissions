class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i:[] for i in range(n)}
        minPath = {i:float('INF') for i in range(n)}
        for from_i, to_i, cost in flights:
            adj[from_i].append([to_i, cost])
        q = deque()
        q.append([src, 0])
        stops = -1
        while stops <= k:
            for _ in range(len(q)):
                air, cost = q.popleft()

                if cost >= minPath[air]:
                    continue
                
                minPath[air] = cost
                for nei, neiCost in adj[air]:
                    q.append([nei, cost+neiCost])
            stops += 1
        
        return minPath[dst] if minPath[dst] < float('INF') else -1