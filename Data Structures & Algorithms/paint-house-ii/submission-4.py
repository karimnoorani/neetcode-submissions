class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        prevMin1 = [0, -1]
        prevMin2 = [0, -1]

        for row in costs:
            min1 = [float('INF'), -1]
            min2 = [float('INF'), -1]

            for i in range(len(row)):
                if i != prevMin1[1]:
                    cost = row[i] + prevMin1[0]
                else:
                    cost = row[i] + prevMin2[0]
                
                if cost < min1[0]:
                    min1, min2 = [cost, i], min1
                elif cost < min2[0]:
                    min2 = [cost, i]
            
            prevMin1, prevMin2 = min1, min2
        
        return prevMin1[0]
            
