class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freqList = [0 for _ in range(len(nums))]

        for num in nums:
            if freqList[num-1] >= 1:
                return num
            
            freqList[num-1] += 1