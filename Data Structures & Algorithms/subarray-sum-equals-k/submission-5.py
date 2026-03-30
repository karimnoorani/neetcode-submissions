class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preMap = {0: 1}
        currSum = 0
        res = 0

        for n in nums:
            currSum += n

            if (currSum-k) in preMap:
                res += preMap[(currSum-k)]
            
            preMap[currSum] = preMap.get(currSum, 0) + 1
        
        return res