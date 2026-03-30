class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals)
        i = 0
        while i < len(intervals):
            interval = intervals[i]
            i += 1
            while i < len(intervals) and interval[1] >= intervals[i][0]:
                interval = [min(interval[0], intervals[i][0]), max(interval[1], intervals[i][1])]
                i += 1
            res.append(interval)
        return res