from bisect import bisect_right
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}
        
        def dfs(i):
            if i == len(days):
                return 0
            
            if i in cache:
                return cache[i]
            
            cache[i] = min(costs[0]+dfs(i+1), costs[1]+dfs(bisect_right(days, days[i]+6)), costs[2]+dfs(bisect_right(days, days[i]+29)))
            return cache[i]
        
        return dfs(0)