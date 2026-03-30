import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        stack = []
        for i, task_info in enumerate(tasks):
            ready_time, process_time = task_info
            stack.append([ready_time, i, process_time])
        
        stack.sort(reverse=True)
        
        time = 1
        heap = []
        res = []
        while stack or heap:
            while stack and time >= stack[-1][0]:
                ready_time, i, process_time = stack.pop()
                heapq.heappush(heap, [process_time, i])
            
            if heap:
                process_time, i = heapq.heappop(heap)
                res.append(i)
                time += process_time
            else:
                time += 1
        
        return res

