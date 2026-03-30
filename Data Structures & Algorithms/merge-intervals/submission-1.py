class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        interval = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] <= interval[1]:
                interval[1] = max(interval[1], intervals[i][1])
            else:
                res.append(interval)
                interval = intervals[i]
        res.append(interval)
        return res