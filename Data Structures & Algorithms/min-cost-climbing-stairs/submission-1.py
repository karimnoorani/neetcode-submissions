class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            
            if i in cache:
                return cache[i]

            cache[i] = min(cost[i] + dfs(i+1), cost[i] + dfs(i+2))
            return cache[i]
        
        return min(dfs(0), dfs(1))
            