class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        
        for i, n in enumerate(nums):
            if (target - n) in numsMap:
                return [numsMap[(target-n)], i]
            numsMap[n] = i
        
        raise Exception()