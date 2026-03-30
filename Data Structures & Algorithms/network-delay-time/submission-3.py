class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)} # src -> [[target, weight]]
        for u, v, t in times:
            adj[u].append([v, t])
        minHeap = [[0, k]] # [weight, node]
        visited = set()

        while minHeap:
            w, node = heapq.heappop(minHeap)
            
            if node in visited:
                continue
            
            visited.add(node)

            if len(visited) == n:
                return w
            
            for nei, neiW in adj[node]:
                if nei in visited:
                    continue
                heapq.heappush(minHeap, [w+neiW, nei])
        
        return -1