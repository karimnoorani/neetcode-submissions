class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        availability_heap = []
        for index, task in enumerate(tasks):
            enqueue_time, _ = task
            availability_heap.append([enqueue_time, index])
        heapq.heapify(availability_heap)

        process_heap = []
        res = []
        time = 1
        while availability_heap or process_heap:
            if not process_heap:
                time = max(time, availability_heap[0][0])
            
            while availability_heap and time >= availability_heap[0][0]:
                _, index = heapq.heappop(availability_heap)
                heapq.heappush(process_heap, [tasks[index][1], index])
            
            process_time, index = heapq.heappop(process_heap)
            res.append(index)
            time += process_time
        
        return res