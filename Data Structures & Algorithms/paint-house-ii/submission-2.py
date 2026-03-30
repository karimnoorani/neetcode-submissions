class Solution:
    def minCostII(self, costs: List[List[int]]) -> int: 
        k = len(costs[0])

        min1 = [0, -1]
        min2 = [0, -1]

        for row in range(len(costs)):
            rowMin1 = [float('INF'), -1]
            rowMin2 = [float('INF'), -1]
            for i in range(k):
                if i == min1[1]:
                    cost_to_paint = min2[0] + costs[row][i]
                else:
                    cost_to_paint = min1[0] + costs[row][i]
                
                if cost_to_paint < rowMin1[0]:
                    rowMin2 = rowMin1
                    rowMin1 = [cost_to_paint, i]
                elif cost_to_paint < rowMin2[0]:
                    rowMin2 = [cost_to_paint, i]
            min1 = rowMin1
            min2 = rowMin2
        
        return min1[0]