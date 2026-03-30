class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixMap = {0: 1}
        res = 0
        total = 0

        for num in nums:
            total += num
            res += prefixMap.get(total-k, 0)
            prefixMap[total] = prefixMap.get(total, 0) + 1
        
        return res