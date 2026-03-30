import heapq

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profits: List[int]) -> int:
        cache = {}
        def dfs(t):
            if t in cache:
                return cache[t]
            
            res = 0
            for start, end, profit in zip(startTime, endTime, profits):
                if start >= t:
                    res = max(res, profit+dfs(end))
            cache[t] = res
            return cache[t]
        return dfs(0)