import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        heap = []
        for point in points:
            x, y = point
            point.insert(0, math.sqrt((x*x) + (y*y)))
            heap.append(point)

        heapq.heapify(heap)
        i = 0
        while i < k:
            res.append(heapq.heappop(heap)[1:])
            i += 1
        
        return res