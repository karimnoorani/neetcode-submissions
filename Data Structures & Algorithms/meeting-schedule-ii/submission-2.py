"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        start, end = [], []

        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        
        start.sort(reverse=True)
        end.sort(reverse=True)

        cur = 0
        while start:
            if start[-1] < end[-1]:
                cur += 1
                start.pop()
            else:
                cur -= 1
                end.pop()
            res = max(res, cur)

        return res
