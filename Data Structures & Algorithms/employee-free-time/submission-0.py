"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        heap = []
        for sched in schedule:
            for s in sched:
                heapq.heappush(heap, [s.start, s.end])
        
        res = []
        while heap:
            start = heap[0][0]
            while heap and start >= heap[0][0]:
                _, end = heapq.heappop(heap)
                start = max(start, end)
            
            if heap:
                res.append(Interval(start, heap[0][0]))
        
        return res