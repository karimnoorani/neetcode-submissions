class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        interval = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] < interval[1]:
                if intervals[i][1] < interval[1]:
                    interval = intervals[i]
                res += 1
            else:
                interval = intervals[i]
        
        return res