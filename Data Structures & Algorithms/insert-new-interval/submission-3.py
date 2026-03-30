class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        res = []
        
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                break
            if i == len(intervals)-1:
                intervals.append(newInterval)
                break
        
        interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= interval[1]:
                interval = [interval[0], max(interval[1], intervals[i][1])]
            else:
                res.append(interval)
                interval = intervals[i]
        res.append(interval)
        return res