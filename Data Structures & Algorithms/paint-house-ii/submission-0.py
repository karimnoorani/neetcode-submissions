class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        k = len(costs[0])
        cache = {}

        def dfs(i, prevColor):
            if i == len(costs):
                return 0
            
            if (i, prevColor) in cache:
                return cache[(i, prevColor)]
            
            res = float('INF')
            for color in range(k):
                if color == prevColor:
                    continue
                res = min(res, costs[i][color]+dfs(i+1, color))
            
            cache[(i, prevColor)] = res
            return cache[(i, prevColor)]
        
        return dfs(0, -1)