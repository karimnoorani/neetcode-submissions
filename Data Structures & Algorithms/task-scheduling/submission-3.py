from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        freqMap = defaultdict(int)
        heap = []
        q = deque()

        for task in tasks:
            freqMap[task] += 1
        
        for task in freqMap:
            heapq.heappush(heap, [-freqMap[task], task])
        
        while heap or q:
            time += 1
            if q and time == q[0][1]:
                task, newTime = q.popleft()
                heapq.heappush(heap, task)
            
            if heap:
                freq, task = heapq.heappop(heap)
                freq += 1
                print(task)
                if freq != 0:
                    q.append([[freq, task], time+n+1])
            else:
                print("IDLE")
        
        return time