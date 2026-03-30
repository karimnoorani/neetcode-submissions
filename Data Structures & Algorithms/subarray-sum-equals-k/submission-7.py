class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = defaultdict(int)
        sumMap[0] = 1
        preSum = 0
        res = 0
        
        for n in nums:
            preSum += n
            if (preSum-k) in sumMap:
                res += sumMap[(preSum-k)]
            
            sumMap[preSum] += 1
        
        return res
            
