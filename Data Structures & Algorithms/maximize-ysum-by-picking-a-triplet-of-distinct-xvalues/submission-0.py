class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        visited = set()
        max_heap = [(-yi, xi) for xi, yi in zip(x, y)]
        heapq.heapify(max_heap)
        res = 0

        while len(visited) < 3:
            while max_heap and max_heap[0][1] in visited:
                heapq.heappop(max_heap)
            
            if not max_heap:
                return -1
            
            yi, xi = heapq.heappop(max_heap)
            res += yi*-1
            visited.add(xi)
        
        return res