class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = {i: [] for i in range(1, n+1)}
        for ui, vi, ti in times:
            adjList[ui].append([ti, vi])

        visited = set()
        heap = [[0, k]]
        
        while heap:
            w, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)
            if len(visited) == n:
                return w
            
            for ti, nei in adjList[node]:
                if nei in visited:
                    continue
                heapq.heappush(heap, [w+ti, nei])
        
        return -1