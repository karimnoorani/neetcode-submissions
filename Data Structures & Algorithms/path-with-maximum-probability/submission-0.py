class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adjList = {node: [] for node in range(n)}

        for succ, edge in zip(succProb, edges):
            a, b = edge
            adjList[a].append([b, succ])
            adjList[b].append([a, succ])
        
        shortest = [float('-inf') for _ in range(n)]
        max_heap = [[-1, start_node]]

        while max_heap:
            succ, node = heapq.heappop(max_heap)
            succ *= -1

            if node == end_node:
                return succ
            
            if succ <= shortest[node]:
                continue
            
            shortest[node] = succ

            for nei, neiSucc in adjList[node]:
                if succ*neiSucc <= shortest[nei]:
                    continue
                heapq.heappush(max_heap, [-succ*neiSucc, nei])

        return 0