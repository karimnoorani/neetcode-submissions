class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for index, num in enumerate(nums):
            if (target-num) in nums_map:
                return [nums_map[target-num], index]

            nums_map[num] = index