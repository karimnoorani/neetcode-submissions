import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {}

        for i in range(1, n+1):
            adjList[i] = []
        
        for time in times:
            ui, vi, ti = time
            adjList[ui].append([vi, ti])
        
        minHeap = [[0, k]]
        shortest = {}
        
        while minHeap:
            w, v = heapq.heappop(minHeap)
            
            if v in shortest:
                continue
            
            shortest[v] = w
            for neighbor in adjList[v]:
                nV, nE = neighbor
                if nV not in shortest:
                    heapq.heappush(minHeap, [(w+nE), nV])
        
        if len(shortest) < n:
            return -1
        
        return max(shortest.values())