import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        position = 0
        currentPass = 0
        heap = []
        currentTrips = [] # [end_point, num_pass]
        for num_pass, start_point, end_point in trips:
            heapq.heappush(heap, [start_point, end_point, num_pass])
        
        while heap:
            start_point, end_point, num_pass = heapq.heappop(heap)
            
            while currentTrips and start_point >= currentTrips[0][0]:
                currentPass -= heapq.heappop(currentTrips)[1]
            
            currentPass += num_pass

            if currentPass > capacity:
                return False
            
            heapq.heappush(currentTrips, [end_point, num_pass])

        return True