class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        cost.insert(0, 0)

        def dfs(i):
            if i > len(cost):
                return float('inf')
            
            if i == len(cost):
                return 0
            
            if i in cache:
                return cache[i]
            
            one = cost[i] + dfs(i+1)
            two = cost[i] + dfs(i+2)

            cache[i] = min(one, two)
            
            return cache[i]
        
        return dfs(0)