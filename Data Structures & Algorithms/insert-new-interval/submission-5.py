class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        curInterval = newInterval
        for start, end in intervals:
            if end < newInterval[0]:
                res.append([start, end])
                continue
            
            if start <= curInterval[1]:
                curInterval[0] = min(curInterval[0], start)
                curInterval[1] = max(curInterval[1], end)
            else:
                res.append(curInterval)
                curInterval = [start, end]
        
        res.append(curInterval)
        return res