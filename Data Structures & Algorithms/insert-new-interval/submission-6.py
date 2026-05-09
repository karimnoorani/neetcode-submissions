class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []

        start, end = intervals[0]
        for newStart, newEnd in intervals[1:]:
            if newStart > end:
                res.append([start, end])
                start, end = newStart, newEnd
            else:
                end = max(end, newEnd)
        res.append([start, end])

        return res