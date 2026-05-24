class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        cache = {}
        def dfs(i, prevColor):
            if i == len(costs):
                return 0
            
            if (i, prevColor) in cache:
                return cache[(i, prevColor)]
            
            cache[(i, prevColor)] = float('inf')
            for color in range(len(costs[i])):
                if color != prevColor:
                    cache[(i, prevColor)] = min(cache[(i, prevColor)], costs[i][color]+dfs(i+1, color))
            
            return cache[(i, prevColor)]
        
        return dfs(0, -1)