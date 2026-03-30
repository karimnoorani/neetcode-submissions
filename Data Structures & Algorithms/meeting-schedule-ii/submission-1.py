"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = [time.start for time in intervals]
        end_times = [time.end for time in intervals]

        start_times.sort()
        end_times.sort()
        
        res = 0
        count = 0

        s, e = 0, 0

        while s < len(start_times):
            if start_times[s] < end_times[e]:
                count += 1
                res = max(res, count)
                s += 1
            else:
                count -= 1
                e += 1

        return res

      