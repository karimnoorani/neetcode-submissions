class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        diff = [(g-c) for g, c in zip(gas, cost)]
        total = 0
        res = 0
        
        for index, num in enumerate(diff):
            if total < 0:
                total = 0
                res = index
            
            total += num
        
        return res