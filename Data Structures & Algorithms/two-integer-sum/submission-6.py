class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i, num in enumerate(nums):
            if (target-num) in numsMap:
                return [numsMap[target-num], i]
            else:
                numsMap[num] = i