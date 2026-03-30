"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        maxCount = 0
        count = 0
        startTimes, endTimes = [], []

        for interval in intervals:
            startTimes.append(interval.start)
            endTimes.append(interval.end)
        
        startTimes.sort()
        endTimes.sort()

        startPointer, endPointer = 0, 0

        while startPointer < len(intervals) and endPointer < len(intervals):
            if endTimes[endPointer] <= startTimes[startPointer]:
                count -= 1
                endPointer += 1
            else:
                count += 1
                maxCount = max(maxCount, count)
                startPointer += 1
        
        return maxCount