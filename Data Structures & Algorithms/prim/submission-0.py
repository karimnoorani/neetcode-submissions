import heapq

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        
        for src, dst, weight in edges:
            adjList[src].append([dst, weight])
            adjList[dst].append([src, weight])

        visited = set([0])

        minHeap = []
        for dst, weight in adjList[0]:
            heapq.heappush(minHeap, [weight, 0, dst])
        
        cost = 0

        while minHeap:
            if len(visited) == n:
                return cost
            
            weight, src, dst = heapq.heappop(minHeap)

            if dst in visited:
                continue
            
            cost += weight
            visited.add(dst)

            src = dst
            for dst, weight in adjList[src]:
                heapq.heappush(minHeap, [weight, src, dst])
        
        return cost if len(visited) == n else -1