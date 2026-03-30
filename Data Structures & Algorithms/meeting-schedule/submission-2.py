"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) == 0:
            return True
            
        intervals.sort(key=lambda x: x.start)
        prev = intervals[0]
        
        for cur in intervals[1:]:
            if cur.start < prev.end:
                return False
            prev = cur
        
        return True