class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        minPath = [float('INF') for _ in range(n)]
        minPath[src] = 0
        for _ in range(k+1):
            tmp = minPath.copy()
            for from_i, to_i, cost in flights:
                if minPath[from_i] == float('INF'):
                    continue
                
                if minPath[from_i] + cost < tmp[to_i]:
                    tmp[to_i] = minPath[from_i] + cost
            
            minPath = tmp
        
        return -1 if minPath[dst] == float('INF') else minPath[dst]