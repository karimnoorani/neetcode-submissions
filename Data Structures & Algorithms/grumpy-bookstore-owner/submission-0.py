class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        maxUnsatisfied = 0
        curUnsatisfied = 0
        res = 0
        for i in range(len(customers)):
            curUnsatisfied += customers[i] if grumpy[i] == 1 else 0
            res += customers[i] if grumpy[i] == 0 else 0
            if i-minutes >= 0 and grumpy[i-minutes] == 1:
                curUnsatisfied -= customers[i-minutes]
            maxUnsatisfied = max(maxUnsatisfied, curUnsatisfied)
        
        return res + maxUnsatisfied