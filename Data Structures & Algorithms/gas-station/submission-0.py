class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        dif = [g-c for g, c in zip(gas, cost)]
        total = 0
        start = 0
        for i, d in enumerate(dif):
            if total < 0:
                total = 0
                start = i
            total += d
        
        return start
