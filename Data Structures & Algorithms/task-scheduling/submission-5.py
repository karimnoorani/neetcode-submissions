import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqMap = defaultdict(int)
        heap = []
        q = deque()
        time = 0

        for task in tasks:
            freqMap[task] += 1
        
        for task, count in freqMap.items():
            heapq.heappush(heap, [-count, task])

        while heap or q:
            time += 1
            if q and time == q[0][1]:
                task_info, _ = q.popleft()
                heapq.heappush(heap, task_info)
            
            if heap:
                freq, task = heapq.heappop(heap)
                freq += 1
                if freq != 0:
                    q.append([[freq, task], time+n+1])
        
        return time