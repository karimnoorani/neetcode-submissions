class Solution:
    def sortColors(self, nums: List[int]) -> None:
        numsMap = {i:0 for i in range(3)}

        for num in nums:
            numsMap[num] += 1
        
        i = 0
        for num in numsMap:
            while numsMap[num] > 0:
                nums[i] = num
                numsMap[num] -= 1
                i += 1
        
        return nums
        """
        Do not return anything, modify nums in-place instead.
        """
        