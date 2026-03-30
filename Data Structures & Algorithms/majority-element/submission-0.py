class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsMap = {}

        for num in nums:
            numsMap[num] = numsMap.get(num, 0) + 1

            if numsMap[num] > len(nums)//2:
                return num