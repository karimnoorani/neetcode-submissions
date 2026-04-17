class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        res = [-1] * len(workers)
        count = 0
        heap = []
        visited = set()

        for wi in range(len(workers)):
            xi, yi = workers[wi]
            for bi in range(len(bikes)):
                xj, yj = bikes[bi]
                heapq.heappush(heap, [abs(xi-xj)+abs(yi-yj), wi, bi])
        
        while heap and count < len(workers):
            d, w, b = heapq.heappop(heap)

            if res[w] != -1 or b in visited:
                continue
            
            res[w] = b
            visited.add(b)
            count += 1
        
        return res