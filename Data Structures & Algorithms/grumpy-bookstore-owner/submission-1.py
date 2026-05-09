class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisified = 0
        maxUnsatisified = 0
        currentUnsatisified = 0
        for index in range(len(customers)):
            currentUnsatisified += customers[index] if grumpy[index] == 1 else 0
            currentUnsatisified += -customers[index-minutes] if index >= minutes and grumpy[index-minutes] == 1 else 0
            satisified += customers[index] if grumpy[index] == 0 else 0
            maxUnsatisified = max(maxUnsatisified, currentUnsatisified)
        return satisified + maxUnsatisified