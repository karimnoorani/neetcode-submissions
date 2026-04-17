class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        res = [-1] * len(workers)
        count = 0
        heap = []
        workersDict = defaultdict(list)
        visited = set()

        for wi in range(len(workers)):
            xi, yi = workers[wi]

            for bi in range(len(bikes)):
                xj, yj = bikes[bi]
                workersDict[wi].append([abs(xi-xj)+abs(yi-yj), bi])
            
            # Sort in reverse to use pop() as getting the smallest distance
            workersDict[wi].sort(reverse=True)
            d, bi = workersDict[wi].pop()
            heapq.heappush(heap, [d, wi, bi])
        
        while heap and count < len(workers):
            d, w, b = heapq.heappop(heap)

            if b in visited:
                while workersDict[w][-1][1] in visited:
                    workersDict[w].pop()
                d, b = workersDict[w].pop()
                heapq.heappush(heap, [d, w, b])
                continue
            
            res[w] = b
            visited.add(b)
            count += 1
        
        return res