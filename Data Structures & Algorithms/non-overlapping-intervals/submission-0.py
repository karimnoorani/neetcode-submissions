class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals) # Sorting by start value
        lastInterval = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < lastInterval[1]:
                if intervals[i][1] < lastInterval[1]:
                    lastInterval = intervals[i]
                count += 1
            else:
                lastInterval = intervals[i]
        return count