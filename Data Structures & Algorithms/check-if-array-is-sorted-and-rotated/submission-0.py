class Solution:
    def check(self, nums: List[int]) -> bool:
        minVal = nums[0]
        minIndex = 0
        
        for i, n in enumerate(nums):
            if n < minVal:
                minVal = n
                minIndex = i
        
        print(minVal, )
        i = minIndex + 1 if minIndex + 1 != len(nums) else 0
        prev = minVal
        while i != minIndex:
            if nums[i] < prev:
                return False
            prev = nums[i]
            i = i + 1 if i + 1 != len(nums) else 0
        
        return True