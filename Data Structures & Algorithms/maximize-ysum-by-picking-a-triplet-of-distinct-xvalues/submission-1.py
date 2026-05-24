class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        used = set()
        max_heap = [(-yi, xi) for xi, yi, in zip(x, y)]
        heapq.heapify(max_heap)
        res = 0

        while len(used) != 3:
            while max_heap and max_heap[0][1] in used:
                heapq.heappop(max_heap)
            
            if not max_heap:
                return -1
            
            yi, xi = heapq.heappop(max_heap)
            yi *= -1

            res += yi
            used.add(xi)
        
        return res
