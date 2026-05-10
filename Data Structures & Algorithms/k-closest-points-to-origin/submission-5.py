class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            heapq.heappush(maxHeap, [-(x*x)-(y*y), x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [(x, y) for c, x, y in maxHeap]