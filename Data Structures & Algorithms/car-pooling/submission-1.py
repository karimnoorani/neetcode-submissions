class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda trip: trip[1])
        end_heap = [] # [end_time, numPass]
        
        for numPass, start, end in trips:
            while end_heap and end_heap[0][0] <= start:
                _, gotOffPass = heapq.heappop(end_heap)
                capacity += gotOffPass
            
            if capacity - numPass < 0:
                return False
            
            heapq.heappush(end_heap, [end, numPass])
            capacity -= numPass
        
        return True