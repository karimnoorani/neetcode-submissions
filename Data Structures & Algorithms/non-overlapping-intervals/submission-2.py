class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curInterval = intervals[0]
        res = 0
        for start, end in intervals[1:]:
            if start >= curInterval[1]:
                curInterval = [start, end]
                continue
            
            if end < curInterval[1]:
                curInterval = [start, end]
            
            res += 1
        
        return res
            
