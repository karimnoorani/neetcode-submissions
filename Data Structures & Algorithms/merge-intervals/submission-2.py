class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curInterval = intervals[0]
        res = []
        for interval in intervals[1:]:
            if interval[0] <= curInterval[1]:
                curInterval[1] = max(curInterval[1], interval[1])
            else:
                res.append(curInterval)
                curInterval = interval
        res.append(curInterval)
        return res