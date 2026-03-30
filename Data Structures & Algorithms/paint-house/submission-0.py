class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        cache = {}
        def dfs(i, prevColor):
            if i == len(costs):
                return 0
            
            if (i, prevColor) in cache:
                return cache[(i, prevColor)]

            res = float('INF')
            for color in range(3):
                if color == prevColor:
                    continue
                res = min(res, costs[i][color]+dfs(i+1, color))
            
            cache[(i, prevColor)] = res
            return cache[(i, prevColor)]
        
        return dfs(0, 4)