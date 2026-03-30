class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preMap = {0: -1}
        pre = 0

        for i in range(len(nums)):
            pre += nums[i]
            
            if pre%k in preMap and i-preMap[pre%k] > 1:
                return True
            
            if pre%k not in preMap:
                preMap[pre%k] = i
        
        return False