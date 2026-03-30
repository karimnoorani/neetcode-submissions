"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startHeap = []
        endHeap = []

        for interval in intervals:
            heapq.heappush(startHeap, interval.start)
            heapq.heappush(endHeap, interval.end)
        
        curMeetings = 0
        res = 0
        while startHeap:
            while endHeap and endHeap[0] <= startHeap[0]:
                curMeetings -= 1
                heapq.heappop(endHeap)
            
            heapq.heappop(startHeap)
            curMeetings += 1
            res = max(res, curMeetings)
        
        return res